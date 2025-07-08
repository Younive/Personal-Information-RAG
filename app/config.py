import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_BASE_DIR = os.path.join(BASE_DIR, "knowledge_base")
VECTOR_DB_DIR = os.path.join(BASE_DIR, "vector_db")

# LLM & Embeddings
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
LLM_MODEL_NAME = 'models/gemini-2.0-flash'
EMBEDDING_MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'

# Text Splitting
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# Retriever
SEARCH_K = 5

CROSS_ENCODER_MODEL = 'cross-encoder/ms-marco-MiniLM-L-6-v2'