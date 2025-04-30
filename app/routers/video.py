# WebSocket 및 HTTP 엔드포인트 정의
from fastapi import APIRouter, Response
from app.config import get_settings
from fastapi.responses import FileResponse
import os
from app.services.frame_extractor import get_frames
from app.utils.logging import logger

settings = get_settings()
router = APIRouter()

@router.get("/video")
async def get_video():
    video_path = os.path.join(settings.MEDIA_DIR, "sample.mp4")
    if os.path.exists(video_path):
        imgs = get_frames("sample.mp4")
        logger.info(f"Video file img extracted")
        return Response(content="video text", media_type='text/plain', status_code=200)
        #return FileResponse(video_path, media_type='video/mp4')
    else:
        return Response(content=f"Video {video_path} not found.", status_code=404)
