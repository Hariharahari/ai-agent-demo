import pytest
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# --- 1. THE SUBJECT (Your Bot) ---
# In a real app, you would import this function from your server.py
def get_pirate_agent():
    llm = ChatNVIDIA(model="meta/llama-3.1-70b-instruct")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a pirate. You MUST say 'Arrr' in every sentence."),
        ("user", "{text}")
    ])
    return prompt | llm | StrOutputParser()

# --- 2. THE TEST (The Inspection) ---
# @pytest.mark.asyncio tells Python this is an AI test (which takes time)
@pytest.mark.asyncio
async def test_pirate_personality():
    print("\n🧪 STARTING TEST: Pirate Persona Check...")
    
    agent = get_pirate_agent()
    
    # We ask a normal question
    response = await agent.ainvoke({"text": "Hello, who are you?"})
    
    print(f"🤖 Bot Replied: {response}")
    
    # --- THE ASSERTION ---
    # We don't care what the rest of the sentence is.
    # We ONLY care if it contains the mandatory keyword "arrr".
    assert "arrr" in response.lower(), "❌ TEST FAILED: Bot forgot to be a pirate!"
    
    print("✅ TEST PASSED: Bot is a pirate.")