project-root/
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI 어플리케이션 진입점
│   ├── config.py              # 환경 변수 및 설정
│   ├── routers/
│   │   ├── __init__.py
│   │   └── video.py           # WebSocket 및 HTTP 엔드포인트 정의
│   ├── services/
│   │   ├── __init__.py
│   │   ├── video_storage.py   # 수신 영상 저장 로직
│   │   ├── broadcaster.py     # 다른 클라이언트로 실시간 전송 로직
│   │   └── frame_extractor.py # 일정 간격 프레임 추출 로직
│   ├── models/
│   │   ├── __init__.py
│   │   └── video_models.py    # 데이터베이스 스키마/목적
│   └── utils/
│       ├── __init__.py
│       └── helpers.py         # 공통 헤플가 함수
├── media/
│   └── videos/                # 업로드된 원본 및 처리된 영상 저장소
├── tests/
│   ├── __init__.py
│   ├── test_video_storage.py  # 서비스 유니트 테스트
│   └── test_frame_extractor.py
├── .env                       # 환경 변수 파일
├── .gitignore
├── requirements.txt           # Python 의존성 목록
└── README.md                  # 프로젝트 개요 및 실행 가지