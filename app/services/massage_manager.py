#
from functools import lru_cache
from fastapi import APIRouter, Response
from app.config import get_settings
from app.utils.logging import logger
import os
import json
import time

settings = get_settings()
'''
push용 message 정의
add_message의 인자로 들어온 메시지를 json형태로 변환하여 message_queue에 추가
get_message로 받아오고
add_message(str) 만 사용하면 됩니다.
'''
class Message:
    def __init__(self):
        self.message_queue = []

    def convert_to_json_message(self, message: str, message_type: int = None, message_time:int = None)->json:

        # message_time이 None이면 현재 시간으로 설정
        if message_time is None:
            message_time = int(time.time())

        if message_type is None:
            message_type = 0

        data = {"message": message, "message_type": message_type, "date": message_time}
        json_data = json.dumps(data)
        return json_data

    def add_message(self, message: str, message_type: int = None, message_time: int = None):
        try:
            json_data = self.convert_to_json_message(message, message_type, message_time)
            self.message_queue.append(json_data)
            logger.info(f"Message added: {json_data}")
        except Exception as e:
            logger.error(f"Error adding message: {e}")

    def get_message(self):
        try:
            if self.message_queue:
                message = self.message_queue.pop(0)
                logger.info(f"Message retrieved: {message}")
                return message
            else:
                logger.info("No messages in queue.")
                return None
        except Exception as e:
            logger.error(f"Error retrieving message: {e}")
            return None

@lru_cache
def get_message() -> Message:
    """
    싱글톤 패턴으로 Message 인스턴스를 공유하기 위한 함수
    """
    return Message()