import asyncio
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver

import dotenv

dotenv.load_dotenv()

memory = MemorySaver()
search = TavilySearchResults(max_results=5)
model = ChatGroq(model="llama-3.1-70b-versatile")


async def search_agent(thread_id, content):
    agent_executor = create_react_agent(model, [search], checkpointer=memory)
    config = {"configurable": {"thread_id": thread_id}}

    async for event in agent_executor.astream_events(
        {"messages": [HumanMessage(content=content)]}, version="v1", config=config
    ):
        kind = event["event"]
        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                print(content, end="")
        elif kind == "on_tool_start":
            print(f"Using tool: {event['name']}...")
            print("")
