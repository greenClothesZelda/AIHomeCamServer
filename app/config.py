'''
.env 변수 설정
사용법
1.의존성 주입
from app.config import get_settings
2.setting변수 설정
settings = get_settings()
3.변수 사용
settings.MEDIA_DIR
'''
# 환경 변수 및 설정
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "VideoChatServer"
    VERSION: str = "0.1.0"
    MEDIA_DIR: str = "./media/videos"
    FRAME_INTERVAL: int = 30
    FRAME_STEP: int = 10
    FRAME_HEIGHT: int = 480
    FRAME_WIDTH: int = 640

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    """
    싱글톤 패턴으로 Settings 인스턴스를 공유하기 위한 함수
    """
    return Settings()