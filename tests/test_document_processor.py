import os
from app.documents_processor import load_and_chunk_documents

def test_document_loading():
    """
    Tests if documents are loaded and chunked correctly.
    """
    chunked_docs = load_and_chunk_documents()
    
    # Pytest uses simple 'assert' statements
    assert chunked_docs is not None
    assert len(chunked_docs) > 0, "Should produce at least one chunk."