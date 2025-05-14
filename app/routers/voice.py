# WebSocket 및 HTTP 엔드포인트 정의
from fastapi import APIRouter, Response
from app.config import get_settings
from fastapi.responses import FileResponse
import os
from app.services.frame_extractor import get_frames
from app.utils.logging import logger
from fastapi import UploadFile, File, HTTPException
from app.routers.socket_cam import websocket_manager  # WebSocket 매니저 가져오기

settings = get_settings()
router = APIRouter()

UPLOAD_DIR = "uploaded_audios"  # 오디오 파일 저장 디렉토리
os.makedirs(UPLOAD_DIR, exist_ok=True)  # 디렉토리가 없으면 생성

@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    """
    클라이언트로부터 오디오 파일을 업로드받아 서버에 저장합니다.
    """
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="올바른 오디오 파일을 업로드하세요.")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        logger.info(f"오디오 파일 저장 완료: {file_path}")

        # WebSocket 클라이언트에게 알림 전송
        #await websocket_manager.broadcast_audio(file_path)
        logger.info("WebSocket 클라이언트에게 오디오 파일 전송 생략")
        # 오디오 파일을 처리하는 함수 호출
        os.remove(file_path)
        logger.info(f"오디오 파일 삭제 완료: {file_path}")
        return Response(status_code=200)
    except Exception as e:
        logger.error(f"파일 저장 중 오류 발생: {e}")
        raise HTTPException(status_code=500, detail="파일 저장 중 오류가 발생했습니다.")

