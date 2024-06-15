# 필요한 라이브러리를 불러옵니다.
import speech_recognition as sr
from pydub import AudioSegment
import os
from tqdm import tqdm
import io
import shutil

# 음성 파일을 텍스트로 변환하는 함수입니다.
def convert_audio_to_text(audio_file_path):
    # Recognizer 객체를 생성합니다.
    recognizer = sr.Recognizer()
    
    # 파일 확장자를 확인합니다.
    file_extension = os.path.splitext(audio_file_path)[1].lower()
    file_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    print(f"파일 확장자 확인: {file_extension}")
    
    # 파일 확장자에 따라 변환을 처리합니다.
    if file_extension == '.mp3':
        print("MP3 파일을 메모리에서 WAV 파일로 변환 중...")
        for _ in tqdm(range(100), desc="MP3 -> WAV 변환"):
            pass  # 변환 시뮬레이션을 위해 딜레이를 추가합니다.
        # MP3 파일을 메모리에서 WAV 파일로 변환합니다.
        audio = AudioSegment.from_mp3(audio_file_path)
        wav_io = io.BytesIO()
        audio.export(wav_io, format='wav')
        wav_io.seek(0)
        audio_file = wav_io
        print("변환 완료")
    elif file_extension == '.wav':
        audio_file = audio_file_path
    else:
        return "지원되지 않는 파일 형식입니다."

    print("음성 파일을 텍스트로 변환 중...")
    for _ in tqdm(range(100), desc="텍스트 변환"):
        pass  # 변환 시뮬레이션을 위해 딜레이를 추가합니다.
    
    # 음성 파일을 불러옵니다.
    with sr.AudioFile(audio_file) as source:
        # 오디오 데이터를 읽습니다.
        audio_data = recognizer.record(source)

        try:
            # 구글 음성 인식 API를 사용하여 음성을 텍스트로 변환합니다.
            text = recognizer.recognize_google(audio_data, language='ko-KR')
            print("변환 성공!")

            # 변환된 텍스트를 파일로 저장합니다.
            text_file_path = f"text_files/{file_name}.txt"
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
            print(f"텍스트가 파일로 저장되었습니다: {text_file_path}")

            return text
        except sr.UnknownValueError:
            # 음성을 인식할 수 없는 경우
            print("음성을 인식할 수 없습니다.")
            return "음성을 인식할 수 없습니다."
        except sr.RequestError as e:
            # API 요청 에러가 발생한 경우
            print(f"API 요청 에러: {e}")
            return f"API 요청 에러: {e}"
        finally:
            # 메모리 해제를 위해 BytesIO 객체를 닫습니다.
            if isinstance(audio_file, io.BytesIO):
                audio_file.close()

# 폴더 생성 함수
def create_folders():
    if not os.path.exists('audio_files'):
        os.makedirs('audio_files')
    if not os.path.exists('text_files'):
        os.makedirs('text_files')

# 음성 파일 변환을 반복적으로 수행합니다.
while True:
    # 사용자로부터 음성 파일 경로를 입력받습니다.
    audio_file_path = input("변환할 음성 파일의 경로를 입력하세요 (종료하려면 'exit' 입력): ")
    
    # 'exit' 명령어가 입력되면 프로그램을 종료합니다.
    if audio_file_path.lower() == 'exit':
        print("프로그램을 종료합니다.")
        break

    # 폴더 생성
    create_folders()

    # 음성 파일을 텍스트로 변환합니다.
    text = convert_audio_to_text(audio_file_path)

    # 변환된 텍스트를 출력합니다.
    if text:
        print(f"변환된 텍스트: {text}")

        # 음성 파일을 audio_files 폴더로 이동합니다.
        shutil.move(audio_file_path, f"audio_files/{os.path.basename(audio_file_path)}")
        print(f"음성 파일이 audio_files 폴더로 이동되었습니다: audio_files/{os.path.basename(audio_file_path)}")
