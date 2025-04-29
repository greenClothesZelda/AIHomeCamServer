# WebSocket 및 HTTP 엔드포인트 정의
from fastapi import APIRouter, Response
from app.config import settings
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/video")
async def get_video():
    video_path = os.path.join(settings.MEDIA_DIR, "sample.mp4")
    print(f"Requested video path: {video_path}")
    if os.path.exists(video_path):
        return FileResponse(video_path, media_type='video/mp4')
    else:
        return Response(content=f"Video {video_path} not found.", status_code=404)
