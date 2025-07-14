# Personal RAG Chatbot for Recruiters

This repository contains the source code for an advanced, conversational AI chatbot designed to assist recruiters and HR professionals. The chatbot leverages a Retrieval-Augmented Generation (RAG) architecture to answer questions about my professional background, skills, and projects based on a curated knowledge base.

The application is built with a modular structure, features a polished, Gemini-inspired UI, includes a comprehensive testing suite, and is ready for serverless deployment.

## ✨ Features

This project goes beyond a naive RAG implementation by incorporating several advanced techniques to improve performance and accuracy:

* **Advanced Retrieval Pipeline**:

  * **Query Expansion**: The user's initial question is expanded into multiple variations using an LLM to retrieve a broader, more relevant set of documents.

  * **Cross-Encoder Re-ranking**: After initial retrieval, a `CrossEncoder` model re-ranks the documents based on their direct relevance to the original query, ensuring the most accurate context is passed to the LLM.

* **Conversational Memory**: The chatbot maintains conversation history, allowing for follow-up questions and a more natural interaction.

* **Polished UI**: A custom-styled Gradio interface that mimics the clean, modern aesthetic of the Google Gemini chatbot.

* **Structured Knowledge Base**: The knowledge base is built from organized markdown files, making it easy to update and maintain.

* **Modular, Testable Codebase**: The application is structured into logical modules for document processing, vector store management, and chain setup, with a corresponding suite of `pytest` tests.

## 🏛️ Architecture

The application follows a modern RAG architecture:

1. **Data Loading & Chunking**: Markdown files from the `knowledge_base/` are loaded and split into context-aware chunks.

2. **Vector Store Creation**: The document chunks are embedded using a `HuggingFace` model and stored in a `ChromaDB` vector store.

3. **Advanced Retrieval**: When a user asks a question:
   a. The question is expanded into multiple variations.
   b. The `ChromaDB` vector store retrieves relevant documents for all question variations.
   c. A `CrossEncoder` model re-ranks the retrieved documents to find the most relevant ones.

4. **Generation**: The top-ranked documents are passed as context, along with the chat history and the question, to a Google `Gemini` LLM, which generates the final answer.

5. **User Interface**: The entire experience is served through a `Gradio` web interface.
