from app.core.database import Base, engine
Base.metadata.create_all(bind=engine)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Import services (you will implement these next)
from app.services.agent import run_agent
from app.services.tools import log_interaction, edit_interaction, fetch_history

app = FastAPI(
    title="AI CRM HCP Module",
    description="AI-powered CRM for Healthcare Professional interactions",
    version="1.0.0"
)

# -----------------------------
# Request Models
# -----------------------------

class ChatRequest(BaseModel):
    message: str

class InteractionRequest(BaseModel):
    hcp_name: str
    topic: str
    follow_up: Optional[str] = None
    summary: Optional[str] = None

class EditRequest(BaseModel):
    id: int
    updates: dict

# -----------------------------
# Health Check
# -----------------------------

@app.get("/")
def root():
    return {"message": "AI CRM Backend is running 🚀"}

# -----------------------------
# Chat-based AI Logging
# -----------------------------

@app.post("/chat-log")
def chat_log(request: ChatRequest):
    try:
        result = run_agent(request.message)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# Form-based Logging
# -----------------------------

@app.post("/log-interaction")
def create_interaction(request: InteractionRequest):
    try:
        result = log_interaction(request.dict())
        return {"status": "saved", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# Edit Interaction
# -----------------------------

@app.put("/edit-interaction")
def update_interaction(request: EditRequest):
    try:
        result = edit_interaction(request.id, request.updates)
        return {"status": "updated", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# Fetch HCP History
# -----------------------------

@app.get("/history/{hcp_name}")
def get_history(hcp_name: str):
    try:
        result = fetch_history(hcp_name)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
