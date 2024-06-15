import os
import shutil
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from datetime import datetime

# audio_files 및 text_files 디렉터리가 없으면 생성합니다
os.makedirs('audio_files', exist_ok=True)
os.makedirs('text_files', exist_ok=True)
os.makedirs('logs', exist_ok=True)  # logs 디렉터리가 없으면 생성합니다

def move_files_to_audio_folder():
    """
    현재 디렉터리에 있는 모든 오디오 파일을 audio_files 디렉터리로 이동합니다.
    """
    supported_formats = ('.mp3', '.wav', '.ogg', '.flv', '.mp4', '.wma')
    for file_name in os.listdir('.'):
        if file_name.lower().endswith(supported_formats):
            shutil.move(file_name, os.path.join('audio_files', file_name))

def log_message(file_name, status, message):
    """
    로그 메시지를 날짜별로 생성된 로그 파일에 기록합니다.

    Parameters:
    file_name (str): 처리한 파일 이름.
    status (str): 성공 또는 실패 상태.
    message (str): 기록할 메시지.
    """
    date_str = datetime.now().strftime('%Y-%m-%d')
    log_file_path = os.path.join('logs', f"{date_str}.log")
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {status} - {file_name.upper()} - {message}\n")

def convert_audio_to_text(audio_file_path):
    """
    오디오 파일을 Google Web Speech API를 사용하여 텍스트로 변환하고, 변환된 텍스트를 텍스트 파일로 저장합니다.

    Parameters:
    audio_file_path (str): 입력 오디오 파일 경로.
    """
    # 파일 확장자를 제외한 파일 이름을 가져옵니다
    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    output_text_file = os.path.join('text_files', f"{base_name}.txt")

    # 변환된 텍스트 파일이 이미 존재하는지 확인합니다
    if os.path.exists(output_text_file):
        print(f"{output_text_file} already exists. Skipping transcription.")
        log_message(audio_file_path, "SKIPPED", f"{output_text_file} already exists.")
        return

    try:
        # 오디오 파일을 메모리 내에서 WAV 형식으로 변환합니다
        file_extension = os.path.splitext(audio_file_path)[1].lower()
        audio = None
        
        if file_extension == '.mp3':
            audio = AudioSegment.from_mp3(audio_file_path)
        elif file_extension == '.wav':
            audio = AudioSegment.from_wav(audio_file_path)
        elif file_extension == '.ogg':
            audio = AudioSegment.from_ogg(audio_file_path)
        elif file_extension == '.flv':
            audio = AudioSegment.from_flv(audio_file_path)
        elif file_extension == '.mp4':
            audio = AudioSegment.from_file(audio_file_path, "mp4")
        elif file_extension == '.wma':
            audio = AudioSegment.from_file(audio_file_path, "wma")
        else:
            raise ValueError("Unsupported file format")
        
        # WAV 형식의 오디오를 BytesIO 객체로 내보냅니다
        wav_io = BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        
        # 음성 인식기를 초기화합니다
        recognizer = sr.Recognizer()

        # BytesIO 객체에서 WAV 데이터를 로드합니다
        with sr.AudioFile(wav_io) as source:
            audio_data = recognizer.record(source)  # 음성 인식기를 사용하여 오디오 파일을 기록합니다

        # 오디오를 텍스트로 변환합니다
        try:
            text = recognizer.recognize_google(audio_data, language="en-US")  # 영어로 변환합니다
            with open(output_text_file, 'w') as f:
                f.write(text)
            print(f"Transcription saved to {output_text_file}")
            log_message(audio_file_path, "SUCCESS", f"Transcription saved to {output_text_file}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            log_message(audio_file_path, "FAILURE", "Speech not understood")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            log_message(audio_file_path, "FAILURE", f"Request error: {e}")

    except ValueError as ve:
        print(ve)
        log_message(audio_file_path, "FAILURE", f"Value error: {ve}")

def main():
    # 모든 지원되는 오디오 파일을 audio_files 디렉터리로 이동합니다
    move_files_to_audio_folder()

    while True:
        # audio_files 디렉터리에 있는 모든 오디오 파일을 나열합니다
        audio_files = os.listdir('audio_files')
        if not audio_files:
            print("No audio files found in the audio_files directory.")
            log_message("None", "INFO", "No audio files found in the audio_files directory.")
        else:
            print("\nAvailable audio files:")
            for idx, file_name in enumerate(audio_files, start=1):
                print(f"{idx}. {file_name}")

        # 사용자가 변환할 오디오 파일 번호를 입력받습니다
        choice = input("Enter the numbers of the audio files to transcribe (comma-separated) or type 'exit' to quit: ")

        if choice.lower() == 'exit':
            break

        try:
            choices = [int(num.strip()) for num in choice.split(',')]
            for choice_num in choices:
                if 1 <= choice_num <= len(audio_files):
                    chosen_file = audio_files[choice_num - 1]
                    chosen_file_path = os.path.join('audio_files', chosen_file)
                    # 선택된 오디오 파일을 텍스트로 변환합니다
                    convert_audio_to_text(chosen_file_path)
                else:
                    print(f"Invalid choice: {choice_num}. Please enter numbers corresponding to the listed files.")
                    log_message("None", "ERROR", f"Invalid choice: {choice_num}")
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers or 'exit'.")
            log_message("None", "ERROR", "Invalid input for file selection")

if __name__ == "__main__":
    main()
