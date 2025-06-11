import os
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from app.config import KNOWLEDGE_BASE_DIR, CHUNK_SIZE, CHUNK_OVERLAP

def add_metadata(document, doc_type):
    document.metadata["doc_type"] = doc_type
    return document

def load_and_chunk_documents():
    current_doc_type = os.path.basename(os.path.normpath(KNOWLEDGE_BASE_DIR))
    print(f"Loading .md files from: '{KNOWLEDGE_BASE_DIR}' with doc_type: '{current_doc_type}'")
    
    documents = []
    try:
        loader = DirectoryLoader(
            path=KNOWLEDGE_BASE_DIR,
            glob="*.md",
            loader_cls=TextLoader,
            loader_kwargs={'encoding': 'utf-8'},
            show_progress=True,
            use_multithreading=False,
        )
        folder_documents = loader.load()

        if folder_documents:
            print(f"Successfully loaded {len(folder_documents)} document(s) from '{KNOWLEDGE_BASE_DIR}'.")
            for doc in folder_documents:
                documents.append(add_metadata(doc, current_doc_type))
        else:
            print(f"No .md documents found in '{KNOWLEDGE_BASE_DIR}'.")
            return [] # Return empty list if no documents

    except FileNotFoundError:
        print(f"Error: The directory '{KNOWLEDGE_BASE_DIR}' was not found. Please check the path.")
        return [] # Return empty list on error
    except Exception as e:
        print(f"An error occurred during document loading: {e}")
        return [] # Return empty list on error

    if not documents: # Check if documents list is empty after loading attempts
        return []

    # Using CharacterTextSplitter as in your notebook. Consider MarkdownTextSplitter for .md specific splitting.
    text_splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunked_documents = text_splitter.split_documents(documents)
    
    print(f"Total number of chunks: {len(chunked_documents)}")
    if documents: # Ensure documents list is not empty before accessing metadata
         print(f"Document types found: {set(doc.metadata.get('doc_type', 'N/A') for doc in documents)}") # Added .get for safety
    return chunked_documents