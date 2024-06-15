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

# 음성 파일을 audio_files 폴더로 이동하는 함수
def move_audio_files_to_folder():
    audio_extensions = ['.mp3', '.wav']
    for file in os.listdir('.'):
        if os.path.isfile(file) and os.path.splitext(file)[1].lower() in audio_extensions:
            shutil.move(file, f"audio_files/{file}")
            print(f"{file}이(가) audio_files 폴더로 이동되었습니다.")

# audio_files 폴더 내의 파일 목록을 보여주고 파일을 선택하는 함수
def select_audio_file():
    files = os.listdir('audio_files')
    if not files:
        print("audio_files 폴더에 파일이 없습니다.")
        return None
    
    print("audio_files 폴더 내의 파일 목록:")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    
    while True:
        selection = input("파일 번호 또는 이름을 입력하세요: ")
        if selection.isdigit():
            idx = int(selection) - 1
            if 0 <= idx < len(files):
                return f"audio_files/{files[idx]}"
        elif selection in files:
            return f"audio_files/{selection}"
        else:
            print("유효하지 않은 입력입니다. 다시 시도하세요.")

# 초기 폴더 생성 및 파일 이동
create_folders()
move_audio_files_to_folder()

# 음성 파일 변환을 반복적으로 수행합니다.
while True:
    # 'exit' 명령어가 입력되면 프로그램을 종료합니다.
    audio_file_path = select_audio_file()
    if not audio_file_path:
        print("프로그램을 종료합니다.")
        break

    # 음성 파일을 텍스트로 변환합니다.
    text = convert_audio_to_text(audio_file_path)

    # 변환된 텍스트를 출력합니다.
    if text:
        print(f"변환된 텍스트: {text}")
