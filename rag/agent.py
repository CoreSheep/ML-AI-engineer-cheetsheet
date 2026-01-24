"""Agent Initialization"""

import os
import asyncio
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.llms.openai import OpenAI
from llama_index.llms.anthropic import Anthropic
from llama_index.core import SimpleDirectoryReader

# Import from local modules
from prompts import CONTEXT, TOOL_DESCRIPTION, TOOL_NAME

# Create LLM instance
# config: provider="openai", model=None
def get_llm(provider="openai", model=None):
    """Get LLM instance based on provider"""
    if provider.lower() == "openai":
        return OpenAI(
            model=model or "gpt-4",
            temperature=0.1,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    elif provider.lower() == "anthropic":
        return Anthropic(
            model=model or "claude-3-sonnet-20240229",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0.1
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}")

# Create query engine
def get_query_engine(index_name="deepseek_ocr_index"):
    """Get the RAG query engine"""
    from embedding.create_index import get_index

    data_path = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    data = SimpleDirectoryReader(data_path, required_exts=[".pdf"]).load_data()
    return get_index(data, index_name).as_query_engine()


def get_agent(provider="openai", model=None, index_name="deepseek_ocr_index"):
    """Returns ReActAgent with specified LLM provider"""
    
    # Get LLM
    llm = get_llm(provider, model)
    
    # Get query engine
    query_engine = get_query_engine(index_name="deepseek_ocr_index")
    if query_engine is None:
        raise ValueError(f"Query engine not found for index: {index_name}")
    
    # Create tools
    tools = [
        QueryEngineTool(
            query_engine,
            metadata=ToolMetadata(
                description=TOOL_DESCRIPTION,
                name=TOOL_NAME,
            ),
        )
    ]
    
    from prompts import CONTEXT, TOOL_DESCRIPTION, TOOL_NAME

    # Create and return agent
    return ReActAgent(
        name=TOOL_NAME,
        description=TOOL_DESCRIPTION,
        tools=tools, 
        llm=llm, 
        system_prompt=CONTEXT, 
        verbose=True
    )


async def main():
    agent = get_agent(provider="openai", model="gpt-4", index_name="deepseek_ocr_index")
    response = await agent.arun("What is DeepSeek-OCR and what problem does it solve?")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())