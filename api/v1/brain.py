from fastapi import APIRouter
from app.brain.reasoning_engine import ReasoningEngine
from app.brain.agent_manager import AgentManager

router = APIRouter()

eng = ReasoningEngine()
agents = AgentManager(eng)

@router.post("/run")
def run_brain(payload: dict):
    return {"result": agents.handle(payload["task"], payload["context"])}
