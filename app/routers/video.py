# WebSocket 및 HTTP 엔드포인트 정의
from fastapi import APIRouter, Response, Form
from app.config import get_settings
from fastapi.responses import FileResponse, JSONResponse
import os
from app.services.frame_extractor import get_frames
from app.utils.logging import logger

from ..baseModel.area import AreaRect

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
async def set_area(x1: float = Form(...), x2: float = Form(...), y1: float = Form(...), y2: float = Form(...)):
    """
    Area rect를 받아 저장합니다.
    """
    area_rect = AreaRect(x1=x1, x2=x2, y1=y1, y2=y2)
    logger.info(f"Recieved Area {area_rect}")
    area_list.append(area_rect.model_dump())
    return Response(content="Area setting received", status_code=200)

@router.get("/setting/area")
async def get_area_list():
    """
    저장된 Area 목록을 반환합니다.
    """
    return JSONResponse(content={"count": len(area_list), "result": area_list}, status_code=200)

@router.get("/clear")
async def clear():
    """
    저장된 Area 목록을 초기화합니다.
    """
    area_list.clear()
    return Response(content="Area list cleared", status_code=200)

@router.post("/clear")
async def clear_post(index: int):
    """
    저장된 Area 목록을 초기화합니다.
    """
    try:
        area_list.pop(index)
        return Response(content="Area list cleared", status_code=200)
    except Exception as e:
        logger.error(f"Error clearing area list: {e}")
        return Response(content="Internal Server Error", status_code=500)