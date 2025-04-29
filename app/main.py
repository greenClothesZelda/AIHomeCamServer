# FastAPI 어플리케이션 진입점
from fastapi import FastAPI
from app.routers.video import router as video_router
from app.config import settings

# 애플리케이션 생성
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

# 라우터 등록
app.include_router(
    video_router,
    prefix="/video",
    tags=["video"],
)

@app.get("/health", tags=["health"])
async def health_check():
    """
    서버 상태 확인용 엔드포인트
    """
    return {"status": "ok", "version": settings.VERSION}