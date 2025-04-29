# 프로젝트 디렉토리 구조
project-root/<br>
├── app/<br>
│   ├── __init__.py<br>
│   ├── main.py                # FastAPI 어플리케이션 진입점<br>
│   ├── config.py              # 환경 변수 및 설정<br>
│   ├── routers/<br>
│   │   ├── __init__.py<br>
│   │   └── video.py           # WebSocket 및 HTTP 엔드포인트 정의<br>
│   ├── services/<br>
│   │   ├── __init__.py<br>
│   │   ├── video_storage.py   # 수신 영상 저장 로직<br>
│   │   ├── broadcaster.py     # 다른 클라이언트로 실시간 전송 로직<br>
│   │   └── frame_extractor.py # 일정 간격 프레임 추출 로직<br>
│   ├── models/<br>
│   │   ├── __init__.py<br>
│   │   └── video_models.py    # 데이터베이스 스키마/목적<br>
│   └── utils/<br>
│       ├── __init__.py<br>
│       └── helpers.py         # 공통 헤플가 함수<br>
├── media/<br>
│   └── videos/                # 업로드된 원본 및 처리된 영상 저장소<br>
├── tests/<br>
│   ├── __init__.py<br>
│   ├── test_video_storage.py  # 서비스 유니트 테스트<br>
│   └── test_frame_extractor.py<br>
├── .env                       # 환경 변수 파일<br>
├── .gitignore<br>
├── requirements.txt           # Python 의존성 목록<br>
└── README.md                  # 프로젝트 개요 및 실행 가지<br>