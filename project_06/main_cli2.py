from gtts import gTTS
import os
import shutil
from datetime import datetime

def text_to_speech(text_file, output_file):
    """
    텍스트 파일을 음성 파일로 변환합니다.
    
    :param text_file: 변환할 텍스트 파일의 경로
    :param output_file: 저장할 음성 파일의 경로
    """
    # 텍스트 파일을 읽습니다
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # gTTS 객체를 생성하여 텍스트를 음성으로 변환합니다 (기본 언어는 영어)
    tts = gTTS(text=text, lang='en')
    
    # 변환된 음성을 파일로 저장합니다
    tts.save(output_file)
    
    # 로그 기록
    log_message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Converted '{text_file}' to '{output_file}'\n"
    log(log_message)

def log(message):
    """
    로그 메시지를 날짜별로 기록합니다.
    
    :param message: 로그에 기록할 메시지
    """
    # log 폴더 생성
    os.makedirs('log', exist_ok=True)
    
    # 날짜별 로그 파일 이름 생성
    log_file_name = datetime.now().strftime("log/%Y-%m-%d.log")
    
    # 로그 메시지 파일에 추가
    with open(log_file_name, 'a', encoding='utf-8') as log_file:
        log_file.write(message)

def main():
    # 디렉토리 생성
    os.makedirs('text_files', exist_ok=True)
    os.makedirs('audio_files', exist_ok=True)

    # 텍스트 파일을 text_files 폴더로 이동
    text_files = [f for f in os.listdir() if f.endswith('.txt')]
    for text_file in text_files:
        shutil.move(text_file, os.path.join('text_files', text_file))

    while True:
        # text_files 폴더 내의 파일 목록을 출력하고 파일을 선택하도록 요청
        print("Select text files from the list below by entering their numbers separated by commas (or type 'exit' to quit):")
        text_files_list = os.listdir('text_files')
        for idx, file in enumerate(text_files_list, 1):
            print(f"{idx}. {file}")

        file_choices = input("Enter the numbers of the files you want to convert to speech: ")

        if file_choices.lower() == "exit":
            print("Exiting program.")
            break

        try:
            file_indices = [int(choice.strip()) - 1 for choice in file_choices.split(',')]
            if not all(0 <= index < len(text_files_list) for index in file_indices):
                raise ValueError("Invalid file number")
        except ValueError as e:
            print("Invalid choice. Please try again.")
            continue

        selected_files = [text_files_list[index] for index in file_indices]
        for selected_file in selected_files:
            text_file_path = os.path.join('text_files', selected_file)
            
            # 음성 파일의 이름을 텍스트 파일의 이름으로 설정
            output_file_name = os.path.splitext(selected_file)[0]
            output_file = os.path.join('audio_files', f"{output_file_name}.mp3")

            if os.path.exists(output_file):
                print(f"Error: The file '{output_file}' already exists. Skipping file.")
            else:
                # 음성 변환 및 저장
                text_to_speech(text_file_path, output_file)
                print(f"Audio file '{output_file}' has been created.")

if __name__ == "__main__":
    main()
