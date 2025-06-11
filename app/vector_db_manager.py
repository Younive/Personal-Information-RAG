# app/vector_store_manager.py
import os
import shutil
from langchain_chroma import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from app.config import VECTOR_DB_DIR, EMBEDDING_MODEL_NAME

def get_vector_store(documents, rebuild_db=False):
    """
    Creates or loads a Chroma vector store.

    Args:
        documents: The documents to add to the store (only used if creating).
        rebuild_db (bool): If True, deletes the existing DB and rebuilds it. 
                         If False, loads the existing DB or creates a new one if it doesn't exist.
    
    Returns:
        A Chroma vector store instance.
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    if rebuild_db and os.path.exists(VECTOR_DB_DIR):
        print(f"Rebuilding DB: Deleting existing vector store at {VECTOR_DB_DIR}")
        shutil.rmtree(VECTOR_DB_DIR)

    if os.path.exists(VECTOR_DB_DIR):
        # DB exists and we are not rebuilding, so load it
        print(f"Loading existing vector store from {VECTOR_DB_DIR}")
        vectorstore = Chroma(
            persist_directory=VECTOR_DB_DIR,
            embedding_function=embeddings
        )
        print(f"Vectorstore loaded with {vectorstore._collection.count()} documents.")
    else:
        # DB does not exist, so create it
        if not documents:
            raise ValueError("No documents provided to create a new vector store.")
        print(f"Creating new vector store at {VECTOR_DB_DIR}")
        vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=VECTOR_DB_DIR
        )
        print(f"Vectorstore created with {vectorstore._collection.count()} documents.")
        
    return vectorstore