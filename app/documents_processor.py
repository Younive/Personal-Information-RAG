import os
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import MarkdownTextSplitter
from app.config import KNOWLEDGE_BASE_DIR, CHUNK_SIZE, CHUNK_OVERLAP

def add_metadata(document, base_path):
    """
    Adds metadata to a document based on its file path, using the
    subfolder as the document type.
    """
    # Get the relative path of the document from the knowledge base root
    relative_path = os.path.relpath(document.metadata['source'], base_path)
    path_parts = relative_path.split(os.sep)

    # If the document is in a subfolder (e.g., 'projects'), use that as the doc_type.
    # Otherwise, assign a general type.
    if len(path_parts) > 1:
        document.metadata["doc_type"] = path_parts[0]
    else:
        document.metadata["doc_type"] = 'general'
        
    return document

def load_and_chunk_documents():
    """
    Loads all .md files from the knowledge_base directory and its subdirectories,
    adds metadata, and splits them into chunks.
    """
    print(f"Loading .md files recursively from: '{KNOWLEDGE_BASE_DIR}'")
    
    documents = []
    try:
        # Use glob="**/*.md" to search recursively in all subdirectories
        loader = DirectoryLoader(
            path=KNOWLEDGE_BASE_DIR,
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={'encoding': 'utf-8'},
            show_progress=True,
            use_multithreading=True,
            recursive=True # Explicitly enable recursive search
        )

        loaded_documents = loader.load()

        if loaded_documents:
            print(f"Successfully loaded {len(loaded_documents)} document(s).")
            # Add metadata to each loaded document
            for doc in loaded_documents:
                documents.append(add_metadata(doc, KNOWLEDGE_BASE_DIR))
        else:
            print(f"No .md documents found in '{KNOWLEDGE_BASE_DIR}'.")
            return []

    except Exception as e:
        print(f"An error occurred during document loading: {e}")
        return []

    # Split documents into smaller chunks
    text_splitter = MarkdownTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunked_documents = text_splitter.split_documents(documents)
    
    print(f"Total number of chunks: {len(chunked_documents)}")
    if documents:
         # This will now show types like {'general', 'projects'}
         print(f"Document types found: {set(doc.metadata.get('doc_type', 'N/A') for doc in documents)}")
         
    return chunked_documents