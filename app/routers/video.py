# WebSocket 및 HTTP 엔드포인트 정의
from fastapi import APIRouter, Response, Request
from app.config import get_settings
from fastapi.responses import FileResponse, JSONResponse
import os
from app.services.frame_extractor import get_frames
from app.utils.logging import logger

settings = get_settings()
router = APIRouter()

band_list = []

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


@router.post("/setting/band")
async def get_band(band_1: int, band_2: int, band_3: int, band_4: int):
    """
    Band 설정을 가져옵니다.
    """
    band = [band_1, band_2, band_3, band_4]
    logger.info(f"Recieved Band {band}")
    band_list.append(band)
    return Response(content="Band setting received", status_code=200)

@router.get("/setting/band")
async def get_band_list():
    """
    Band 리스트를 JSON 형태로 반환합니다.
    """
    return JSONResponse(content={"band_list": band_list}, status_code=200)