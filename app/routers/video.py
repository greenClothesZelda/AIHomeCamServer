# WebSocket 및 HTTP 엔드포인트 정의
from fastapi import APIRouter, Response, Request
from app.config import get_settings
from fastapi.responses import FileResponse, JSONResponse
import os
from app.services.frame_extractor import get_frames
from app.utils.logging import logger

settings = get_settings()
router = APIRouter()

area_list = []

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


@router.post("/setting/area")
async def get_area(x1: float, y1: float, x2: float, y2: float):
    """
    저장된 Area 목록을 가져옵니다.

    [x1, y1, x2, y2]
    x1, y1, x2, y2 = 0 ~ 1
    """
    area = [x1, y1, x2, y2]
    logger.info(f"Recieved Area {area}")
    area_list.append(area)
    return Response(content="Area setting received", status_code=200)

@router.get("/setting/area")
async def get_area_list():
    """
    저장된 Area 목록을 JSON 형태로 반환합니다.
    """
    return JSONResponse(content={"area_list": area_list}, status_code=200)