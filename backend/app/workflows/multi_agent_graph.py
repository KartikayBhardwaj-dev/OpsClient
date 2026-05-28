from langgraph.graph import StateGraph
from langgraph.graph import END
from app.workflows.state import GraphState
from app.agents.supervisor_agent import SupervisorAgent
from app.agents.research_agent import ResearchAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.support_agent import SupportAgent
from app.agents.summary_agent import SummaryAgent

supervisor = SupervisorAgent()
research_agent = ResearchAgent()
analytics_agent = AnalyticsAgent()
support_agent = SupportAgent()
summary_agent = SummaryAgent()

async def supervisor_node(state: GraphState):
    decision = await supervisor.decide_agent(
        state["user_input"]
    )
    return {
        "selected_agent": decision
    }


async def research_node(state: GraphState):
    result = await research_agent.run(
        state["user_input"]
    )

    return {
        "research": result
    }

async def analytics_node(state: GraphState):
    result = await analytics_agent.run(
        state["user_input"]
    )
    return {
        "research": result
    }

async def support_node(
    state: GraphState
):
    result = await support_agent.run(
        state["user_input"]
    )
    return {
        "research": result
    }

async def summary_node(
    state: GraphState
):

    final_summary = await summary_agent.run(
        state["research"]
    )
    return {
        "summary": final_summary
    }

def route_agent(
    state: GraphState
):

    decision = state["selected_agent"]
    if "research" in decision:
        return "research"
    if "analytics" in decision:
        return "analytics"
    return "support"


workflow = StateGraph(GraphState)

workflow.add_node(
    "supervisor", supervisor_node
)

workflow.add_node(
    "research", research_node
)

workflow.add_node(
    "analytics", analytics_node
)

workflow.add_node(
    "support", support_node
)

workflow.add_node(
    "summary", summary_node
)

workflow.set_entry_point("supervisor")

workflow.add_conditional_edges(
    "supervisor",
    route_agent,
    {
        "research": "research",
        "analytics": "analytics",
        "support": "support"
    }
)


workflow.add_edge(
    "research", "summary"
)

workflow.add_edge(
    "analytics", "summary"
)
workflow.add_edge(
    "support", "summary"
)

workflow.add_edge(
    "summary", END
)

graph = workflow.compile()