'''
logger 사용방법

1. 의존성 주입
from app.utils.logging import logger
2. logger.info("로그 메시지")
'''
import logging
import os

LOG_FILE_PATH = 'logs/app.log'
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode='a'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('fastapi_app')
logger.info('Logging started')