# WebSocket 및 HTTP 엔드포인트 정의
from fastapi import APIRouter, WebSocket, Depends, HTTPException
from app.config import settings

router = APIRouter()

@router.get("/video")
async def get_video():
    return {"message": "Video endpoint"}