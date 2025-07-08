import pytest
from app.main import conversation_chain

def test_conversation_chain_produces_answer():
    """
    Tests if the full RAG chain can be invoked and returns a valid answer.
    """
    if conversation_chain is None:
        pytest.skip("Conversation chain not initialized, skipping test.")

    question = "What was the main challenge in the Restaurant Recommendation API project?"
    
    # invoke the chain
    result = conversation_chain.invoke({"question": question})

    # assert that the result is in the expected format
    assert "answer" in result
    assert isinstance(result["answer"], str)
    assert len(result["answer"]) > 0 # Ensure the answer is not empty
    
    print(f"\nIntegration Test Passed. Question: '{question}'")
    print(f"Answer: '{result['answer']}'")