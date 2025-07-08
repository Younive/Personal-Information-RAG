from langchain.chains import ConversationalRetrievalChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.retrievers import BaseRetriever
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from sentence_transformers import CrossEncoder
from langchain_core.vectorstores import VectorStoreRetriever
from app.prompts import SYSTEM_PROMPT_CONTENT, EXPANSION_PROMPT_TEMPLATE
from app.config import CROSS_ENCODER_MODEL

class AdvancedRetriever(BaseRetriever):
    """
    A retriever that combines query expansion and cross-encoder re-ranking.
    """
    vectorstore_retriever: VectorStoreRetriever
    llm: BaseChatModel
    top_k: int = 5

    def _get_relevant_documents(self, query: str, *, run_manager):
        reranker = CrossEncoder(CROSS_ENCODER_MODEL)
        expansion_prompt = ChatPromptTemplate.from_template(EXPANSION_PROMPT_TEMPLATE)
        expansion_chain = expansion_prompt | self.llm | StrOutputParser()
        expanded_queries_str = expansion_chain.invoke({"question": query}, config={"run_name": "QueryExpansion"})
        all_queries = [query] + expanded_queries_str.strip().split('\n')
        
        all_retrieved_docs = []
        for q in all_queries:
            # Retrieve documents for each expanded query
            all_retrieved_docs.extend(self.vectorstore_retriever.get_relevant_documents(q))

        unique_docs_dict = {doc.page_content: doc for doc in all_retrieved_docs}
        unique_docs = list(unique_docs_dict.values())
        
        if not unique_docs:
            return []

        doc_texts = [doc.page_content for doc in unique_docs]
        query_doc_pairs = [[query, doc_text] for doc_text in doc_texts]
        
        scores = reranker.predict(query_doc_pairs)
        
        doc_scores = list(zip(unique_docs, scores))
        doc_scores.sort(key=lambda x: x[1], reverse=True)
        
        reranked_docs = [doc for doc, score in doc_scores[:self.top_k]]
        
        return reranked_docs

QA_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT_CONTENT),
    ("human", "Given the following context and question, please provide an answer.\n\nContext:\n{context}\n\nQuestion:\n{question}")
])


def get_conversational_chain(vector_store, llm, memory):
    """
    Builds and returns the conversational RAG chain using the AdvancedRetriever.
    """
    # Create the base vector store retriever. It should retrieve more documents initially 
    # to give the expansion and re-ranking process a good pool to work with.
    base_retriever = vector_store.as_retriever(search_kwargs={"k": 10})

    # Initialize your new AdvancedRetriever, passing it the base retriever and the LLM.
    # It will return the final top 5 most relevant documents.
    advanced_retriever = AdvancedRetriever(
        vectorstore_retriever=base_retriever, 
        llm=llm,
        top_k=5
    )

    # Create the final chain using the advanced_retriever
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, 
        retriever=advanced_retriever,
        memory=memory, 
        combine_docs_chain_kwargs={"prompt": QA_PROMPT_TEMPLATE}
    )
    
    return conversation_chain