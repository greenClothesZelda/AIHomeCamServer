import os
from TTS.api import TTS
import asyncio

UPLOAD_DIR = "media/voices/uploads"
OUTPUT_DIR = "media/voices/ouputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 모델 로드 (한 번만)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

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