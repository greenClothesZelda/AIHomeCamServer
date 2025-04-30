from fastapi import APIRouter, Response
from app.config import get_settings
from app.utils.logging import logger
import json
from app.services.massage_manager import get_message

messages = get_message()
settings = get_settings()
router = APIRouter()

@router.get("/message")
async def message():
    """
    메시지 전송 엔드포인트
    """
    try:
        message = messages.get_message()
        if message:
            return Response(content=message, media_type='application/json', status_code=200)
        else:
            return Response(content="No messages in queue.", status_code=204)
    except Exception as e:
        logger.error(f"Error retrieving message: {e}")
        return Response(content="Internal Server Error", status_code=500)

@router.post("/message")
async def message_post(message: str):
    """
    메시지 전송 엔드포인트
    """
    try:
        messages.add_message(message)
        return Response(content="Message added to queue.", status_code=200)
    except Exception as e:
        logger.error(f"Error adding message: {e}")
        return Response(content="Internal Server Error", status_code=500)