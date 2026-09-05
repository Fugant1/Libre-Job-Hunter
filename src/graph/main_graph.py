from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
from typing import TypedDict, List

class AgentState(TypedDict):
    input: str
    output: str
    tool_calls: list[dict]
    tool_results: list[dict]
    next_step: str
    retries: int

class JobGraph:
    def __init__(self, api_key: str, ai_model: str, tools: List[str], **kwargs):
        self.ai_model: str = ai_model
        self.api_key: str = api_key
        self.possible_tools: List[str] = tools
        self.graph = None

    def create_graph(self):
        builder = StateGraph(AgentState)

        builder.add_node()
        builder.add_node()

        builder.set_entry_point() 

        builder.add_edge()
        builder.add_edge()

        return builder.compile()