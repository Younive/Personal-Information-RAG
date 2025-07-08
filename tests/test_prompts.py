import pytest
from langchain_core.prompts import ChatPromptTemplate
from app.prompts import SYSTEM_PROMPT_CONTENT 

def test_qa_prompt_formatting():
    """
    Tests if the main QA prompt can be formatted correctly.
    """
    qa_prompt_template = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT_CONTENT),
        ("human", "Context: {context}\n\nQuestion: {question}")
    ])
    
    try:
        # Attempt to format the prompt with dummy data
        qa_prompt_template.format(
            context="This is the context.",
            question="This is the question."
        )
    except Exception as e:
        pytest.fail(f"QA prompt formatting failed with an exception: {e}")