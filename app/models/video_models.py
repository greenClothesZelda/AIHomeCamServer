import cv2
import time
from ultralytics import YOLO

model = YOLO("../../test/yolo11l.pt")

# box기반 AABB 충돌 감지
def is_aabb_collision(box1, box2):
    """
    box1, box2: [x_min, y_min, x_max, y_max] 형식의 길이 4 배열
    """
    return not (
        box1[2] <= box2[0] or  # box1의 x_max <= box2의 x_min
        box1[0] >= box2[2] or  # box1의 x_min >= box2의 x_max
        box1[3] <= box2[1] or  # box1의 y_max <= box2의 y_min
        box1[1] >= box2[3]     # box1의 y_min >= box2의 y_max
    )

# 이미지에서 person 객체만 추출
def getPersonRect(img):
    # conf = 정확도, 0.5 이상의 확률로 분류된 객체만 사용
    result = model.predict(img, verbose=False, save=False, conf=0.5)[0]
    ret = []
    for box in result.boxes:
        if box.cls.item() == 0:
            temp = box.xyxy.cpu().numpy()
            ret.append([int(temp[0][0]), int(temp[0][1]), int(temp[0][2]), int(temp[0][3])])
    return ret

# 객체와 금지 구역 BOX사이 충돌 감지
def checkBanAera(img, areas):
    ret = getPersonRect(img)
    if ret:
        result = []
        for box, bi in ret:
            for area, ai in areas:
                if is_aabb_collision(box, area):
                    result.append((bi, ai))
        return True, result
    else:
        return False, []

# 테스트용 main 함수
if __name__ == "__main__":
    print("video_models main")
    cap = cv2.VideoCapture("../../test/test_video_2.mp4")
    while True:
        ret, frame = cap.read()
        if ret:
            start = time.time()
            result = getPersonRect(frame)
            if len(result) != 0:
                for box in result:
                    cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.imshow("result", frame)
            end = time.time()
            dt = int((end - start) * 1000)
            print(f"took {dt} ms")
            cv2.waitKey(1)
        else:
            break

