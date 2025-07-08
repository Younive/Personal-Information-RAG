import pytest
from unittest.mock import create_autospec, ANY # <-- Import ANY
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.language_models import BaseChatModel
from langchain_core.prompt_values import ChatPromptValue
from langchain_core.messages import HumanMessage
from app.prompts import EXPANSION_PROMPT_TEMPLATE

# Import your AdvancedRetriever class
from app.llm_chain_setup import AdvancedRetriever 

def test_advanced_retriever_logic():
    # create Mock Components
    mock_llm = create_autospec(BaseChatModel, instance=True)
    mock_llm.invoke.return_value = "expanded question 1\nexpanded question 2"

    mock_vectorstore_retriever = create_autospec(VectorStoreRetriever, instance=True)
    docs = [Document(page_content="doc 1"), Document(page_content="doc 2")]
    mock_vectorstore_retriever.get_relevant_documents.return_value = docs

    # initialize the retriever
    advanced_retriever = AdvancedRetriever(
        vectorstore_retriever=mock_vectorstore_retriever,
        llm=mock_llm,
        top_k=1
    )

    # run the test
    original_query = "original question"
    result = advanced_retriever._get_relevant_documents(original_query, run_manager=None)

    # assert the expected behavior
    
    # construct the expected ChatPromptValue object
    expected_prompt = EXPANSION_PROMPT_TEMPLATE.format(question=original_query)
    expected_prompt_value = ChatPromptValue(messages=[HumanMessage(content=expected_prompt)])
    
    # assert that the mock was called with the correct prompt, and ANY config dictionary
    mock_llm.invoke.assert_called_once_with(expected_prompt_value, config=ANY)
    
    # assert that the vectorstore retriever was called with the expanded queries
    assert mock_vectorstore_retriever.get_relevant_documents.call_count == 3
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], Document)