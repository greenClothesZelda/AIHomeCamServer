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