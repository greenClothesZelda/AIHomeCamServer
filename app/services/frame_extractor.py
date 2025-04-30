

import cv2
import os
from app.config import get_settings

settings = get_settings()


def get_frames(name_video):
    video_path = os.path.join(settings.MEDIA_DIR, name_video)

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file {video_path} not found.")

    #동영상 파일 열기
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    frame = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    result = [] #일단 list이지만 width와 height 어떻게 할지 정해지면 np.zeros로 할 예정

    while frame < total_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, img = cap.read()

        if not ret:
            break

        result.append(img)
        frame += settings.FRAME_STEP

    return result

