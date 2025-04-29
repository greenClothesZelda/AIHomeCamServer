# 환경 변수 및 설정
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "VideoChatServer"
    VERSION: str = "0.1.0"
    # 영상 저장 디렉토리
    MEDIA_DIR: str = "./media/videos"
    # 프레임 추출 간격 (N 프레임마다)
    FRAME_INTERVAL: int = 300

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()