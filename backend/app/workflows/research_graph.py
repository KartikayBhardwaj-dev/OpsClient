from langgraph.graph import StateGraph
from langgraph.graph import END
from app.workflows.state import GraphState
from app.workflows.nodes.planner import planner_node
from app.workflows.nodes.researcher import researcher_node
from app.workflows.nodes.summary import summarizer_node

workflow = StateGraph(GraphState)

workflow.add_node(
    "planner", planner_node
)

workflow.add_node(
    "researcher", researcher_node
)

workflow.add_node(
    "summarizer", summarizer_node
)

workflow.set_entry_point("planner")
workflow.add_edge(
    "planner", "researcher"
)

workflow.add_edge(
    "researcher", "summarizer"
)

workflow.add_edge(
    "summarizer", END
)

graph = workflow.compile()