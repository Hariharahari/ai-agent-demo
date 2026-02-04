import pytest
from dotenv import load_dotenv
# Import your actual agent from main.py if possible, or redefine it here for the test
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_test_agent():
    llm = ChatNVIDIA(model="meta/llama-3.1-70b-instruct")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a pirate. Always say 'Arrr'."),
        ("user", "{text}")
    ])
    return prompt | llm | StrOutputParser()

@pytest.mark.asyncio
async def test_pirate_mode():
    agent = get_test_agent()
    response = await agent.ainvoke({"text": "Hello"})
    assert "arrr" in response.lower()