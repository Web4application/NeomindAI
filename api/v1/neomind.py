from fastapi import APIRouter
from app.neomind.emotion_engine import EmotionEngine

router = APIRouter()
emo = EmotionEngine()

@router.post("/emotion")
def check_emotion(payload: dict):
    return {"mood": emo.detect(payload["embedding"])}
