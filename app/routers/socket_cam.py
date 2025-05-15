#나중에 커지면 따로 socket directory를 만들어서 관리할 것

from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect
from torch.nn.parallel.comm import broadcast

from app.utils.logging import logger
from asyncio import sleep
import os
from typing import List

router = APIRouter()

class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"WebSocket connected: {websocket.client}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info(f"WebSocket disconnected: {websocket.client}")

    async def broadcast_audio(self, file_path: str):
        """
        업로드된 오디오 파일을 모든 WebSocket 클라이언트에게 전송합니다.
        """
        if os.path.exists(file_path):
            with open(file_path, "rb") as audio_file:
                audio_data = audio_file.read()
                for connection in self.active_connections:
                    try:
                        await connection.send_bytes(audio_data)
                        logger.info(f"Sent file to {connection.client}: {file_path}")
                    except Exception as e:
                        logger.error(f"Error sending file to {connection.client}: {e}")
        else:
            logger.error(f"File not found: {file_path}")

websocket_manager = WebSocketManager()

@router.get("/")
async def get():
    """
    WebSocket 엔드포인트
    """
    return {"message": "WebSocket endpoint"}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)
    try:
        while True:
            # WebSocket 연결 유지
            await sleep(1)
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        if not websocket.client_state.DISCONNECTED:
            await websocket.close()

