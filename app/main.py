import gradio as gr
from app.documents_processor import load_and_chunk_documents
from app.vector_db_manager import get_vector_store
from app.llm_chain_setup import get_conversational_chain
from app.config import KNOWLEDGE_BASE_DIR, VECTOR_DB_DIR, GEMINI_API_KEY, LLM_MODEL_NAME
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
import os

css_path = os.path.join(os.path.dirname(__file__), 'css', 'style.css')

# --- Global Setup (Consider doing this once on app startup) ---
print("Starting application setup...")
# By default, it will now load the DB if it exists, not rebuild it.
# Set rebuild_db=True only when you've updated your knowledge_base files.
REBUILD_VECTOR_DB_ON_STARTUP = True # Set to False for faster startups after the first run

chunked_docs = []
if REBUILD_VECTOR_DB_ON_STARTUP or not os.path.exists(VECTOR_DB_DIR):
    chunked_docs = load_and_chunk_documents()

if not chunked_docs and (REBUILD_VECTOR_DB_ON_STARTUP or not os.path.exists(VECTOR_DB_DIR)):
    print("No documents were loaded. Cannot initialize vector store or chain.")
    conversation_chain = None
else:
    vectorstore = get_vector_store(chunked_docs, rebuild_db=True)
    
    # Initialize LLM and Memory here
    llm = ChatGoogleGenerativeAI(model=LLM_MODEL_NAME, temperature=0.0, api_key=GEMINI_API_KEY)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True, output_key='answer') # Important: add output_key
    
    # Get the fully configured chain from your setup file
    conversation_chain = get_conversational_chain(vectorstore, llm, memory)

print("Application setup complete.")
# --- End Global Setup ---

def chat_with_rag(question, history_tuples):

    if conversation_chain is None:
        return "Sorry, the RAG system is not initialized due to an error in loading documents."

    try:
        result = conversation_chain.invoke({"question": question})
        return result["answer"]
    except Exception as e:
        print(f"Error during chat: {e}")
        return "Sorry, an error occurred while processing your question."

# chatbot css
with open(css_path, "r", encoding="utf-8") as f:
    custom_css = f.read()

initial_bot_greeting = "Hello! You can ask me questions about my builder's experiences and projects. What would you like to know?"


# Main launch function
def launch_app():
    if not KNOWLEDGE_BASE_DIR or not os.listdir(KNOWLEDGE_BASE_DIR):
         print("Knowledge base is empty or not found. The chatbot might not function correctly.")
    print("Launching Gradio app...")
    # The fn for ChatInterface with type="messages" expects `message` and `history_messages`
    # `history_messages` will be a list of dictionaries: [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
    def chat_interface_fn(message, history_messages):
        response = chat_with_rag(message, history_messages) # history_messages is for context, but chain uses its own memory.
        return response

    # Create a Gradio Chatbot instance with the initial greeting

    live_chatbot = gr.Chatbot(
        elem_id="screen_fit_chatbot",
        value=[{"role": "assistant", "content": initial_bot_greeting}], # Correct for type="messages"
        label="RAG Chatbot",
        bubble_full_width=False,
        type="messages"
    )
    
    view = gr.ChatInterface(
        fn=chat_interface_fn, # Use the function adapted for message, history_list_of_dicts
        chatbot=live_chatbot, # Pass the pre-configured chatbot
        css=custom_css,
        type="messages"
    )
    view.launch(inbrowser=True, debug=True) # Set share=True for a public link if needed

if __name__ == '__main__':
    launch_app()