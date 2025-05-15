# FastAPI 어플리케이션 진입점
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.video import router as video_router
from app.routers.message import router as message_router
from app.routers.socket_cam import router as socket_router
from app.routers.voice import router as voice_router
from app.config import get_settings

from app.utils.logging import logger

settings = get_settings()


# 애플리케이션 생성
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 Origin 허용
    allow_credentials=False,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)
# 라우터 등록
app.include_router(
    video_router,
    prefix="/video",
    tags=["api"],
)

app.include_router(
    message_router,
    prefix="/message",
    tags=["api"],
)

app.include_router(
    socket_router,
    prefix="/socket",
    tags=["socket"],
)
app.include_router(
    voice_router,
    prefix="/voice",
    tags=["voice"],
)

@app.get("/health", tags=["health"])
async def health_check():
    """
    서버 상태 확인용 엔드포인트
    """
    logger.info("Health check endpoint called")
    return {"status": "ok", "version": settings.VERSION}