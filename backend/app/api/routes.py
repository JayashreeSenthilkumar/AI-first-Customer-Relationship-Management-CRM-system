from fastapi import APIRouter
from app.services.agent import run_agent
from app.services.tools import log_interaction, edit_interaction, fetch_history

router = APIRouter()

@router.post("/chat-log")
def chat_log(data: dict):
    return run_agent(data["message"])

@router.post("/log-interaction")
def create(data: dict):
    return log_interaction(data)

@router.put("/edit-interaction")
def edit(data: dict):
    return edit_interaction(data["id"], data["updates"])

@router.get("/history/{hcp_name}")
def history(hcp_name: str):
    return fetch_history(hcp_name)
