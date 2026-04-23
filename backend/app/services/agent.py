from langgraph.graph import StateGraph
from typing import TypedDict

from app.services.tools import log_interaction, edit_interaction, fetch_history
from app.services.llm import extract_interaction_data

# -----------------------------
# Define State
# -----------------------------
class AgentState(TypedDict):
    input: str
    output: dict


# -----------------------------
# Agent Logic Node
# -----------------------------
def agent_node(state: AgentState):
    user_input = state["input"].lower()

    # ---- Edit Case ----
    if "edit" in user_input:
        result = edit_interaction(1, {"topic": "updated via AI"})
        return {"output": result}

    # ---- History Case ----
    elif "history" in user_input:
        result = fetch_history("Dr. Ravi")
        return {"output": result}

    # ---- Default: Log Interaction ----
    else:
        extracted = extract_interaction_data(state["input"])
        result = log_interaction(extracted)
        return {"output": result}


# -----------------------------
# Build LangGraph
# -----------------------------
builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.set_entry_point("agent")

graph = builder.compile()


# -----------------------------
# Run Agent Function
# -----------------------------
def run_agent(user_input: str):
    response = graph.invoke({"input": user_input})
    return response["output"]
