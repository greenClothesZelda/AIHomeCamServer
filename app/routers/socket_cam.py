#나중에 커지면 따로 socket directory를 만들어서 관리할 것

from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect
from app.utils.logging import logger

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
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
            logger.info(data)


    except WebSocketDisconnect:

        logger.info("WebSocket disconnected")

    except Exception as e:

        logger.error(f"Unexpected error: {e}")

    finally:
        if not websocket.client_state.DISCONNECTED:
            await websocket.close()
