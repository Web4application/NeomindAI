from fastapi import APIRouter
from app.memory.memory_store import MemoryStore
from app.config import Config

router = APIRouter()
store = MemoryStore(Config.VECTOR_DB_URL)

@router.post("/")
def save_memory(payload: dict):
    return store.save_memory(payload["embedding"], payload["metadata"])

@router.post("/search")
def search_memory(payload: dict):
    return store.retrieve(payload["embedding"])
