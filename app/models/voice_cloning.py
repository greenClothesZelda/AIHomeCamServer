import os
from TTS.api import TTS
import asyncio

UPLOAD_DIR = "media/voices/uploads"
OUTPUT_DIR = "media/voices/ouputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 모델 로드 (한 번만)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

import openai

# OpenAI API 키 설정
openai.api_key = "your_openai_api_key"

# LLM을 통한 상황 분석 및 경고 메시지 생성 함수
def analyze_situation_and_generate_warning(frame_data):
    # frame_data는 영상에서 감지된 데이터 (예: 'child in restricted area', 'child in dangerous behavior' 등)
    # 이 데이터를 LLM에 전달하여 분석 및 경고 메시지 생성

    # LLM에 전달할 프롬프트 생성
    prompt = f"Based on the following data from a home camera, analyze the situation and generate an appropriate warning message for the child. Situation data: {frame_data}"

    # OpenAI API 호출하여 분석 및 경고 메시지 생성
    response = openai.Completion.create(
        engine="text-davinci-003",  # 원하는 모델 선택
        prompt=prompt,
        max_tokens=100  # 경고 메시지의 길이
    )

    # 생성된 경고 메시지 반환
    return response.choices[0].text.strip()

# 예시: 영상에서 감지된 데이터 (예: '아이 금지 구역 접근', '위험한 행동 발생')
frame_data = "The child is approaching a restricted area. The child seems unaware of the danger."
warning_message = analyze_situation_and_generate_warning(frame_data)

print(warning_message)

async def generate_tts_from_stored_voice(speaker_wav_filename, sentences):
    speaker_path = os.path.join(UPLOAD_DIR, speaker_wav_filename)

    if not os.path.exists(speaker_path):
        return {
            "message": "voice file do not exist.",
            "files": []  # 항상 'files' 키 포함
        }

    generated_files = []

    for idx, text in enumerate(sentences):
        output_filename = f"output_{idx}.wav"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        try:
            tts.tts_to_file(
                text=text,
                file_path=output_path,
                speaker_wav=speaker_path,
                language="en"
            )
            generated_files.append(output_filename)
        except Exception as e:
            generated_files.append(f"Error: {str(e)}")

    return {
        "message": "TTS transforming complete",
        "files": generated_files
    }

SPEAKER_FILENAME = "test.wav"

SENTENCES = [
    "Hello, this is the test voice"
]

#test
async def main():
    print("generate_tts_from_stored_voice 테스트 시작")

    result = await generate_tts_from_stored_voice(SPEAKER_FILENAME, SENTENCES)

    print("결과 메시지:", result["message"])
    print("생성된 파일 목록:")
    for file in result["files"]:
        if file.startswith("Error:"):
            print(" - 오류 발생:", file)
        else:
            print(" -", os.path.join(OUTPUT_DIR, file))

if __name__ == "__main__":
    asyncio.run(main())
