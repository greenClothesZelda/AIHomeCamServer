#나중에 커지면 따로 socket directory를 만들어서 관리할 것

from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect
from app.utils.logging import logger
from asyncio import sleep
import os

router = APIRouter()

@router.get("/")
async def get():
    """
    WebSocket 엔드포인트
    """
    return {"message": "WebSocket endpoint"}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info(f"WebSocket connected: {websocket.client}")
    try:
        # 2초 대기 후 sample_audio.mp3 파일 전송
        await sleep(2)
        file_path = "videos/sample_audio.mp3"
        if os.path.exists(file_path):
            with open(file_path, "rb") as audio_file:
                audio_data = audio_file.read()
                await websocket.send_bytes(audio_data)
                logger.info(f"Sent file: {file_path}")
        else:
            logger.error(f"File not found: {file_path}")

    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")

    finally:
        if not websocket.client_state.DISCONNECTED:
            await websocket.close()

