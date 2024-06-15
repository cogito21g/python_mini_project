import os
from gtts import gTTS

def ensure_directories():
    """
    오디오 파일과 텍스트 파일을 저장할 디렉토리가 존재하지 않으면 생성합니다.
    """
    if not os.path.exists("audio_files"):
        os.makedirs("audio_files")
    if not os.path.exists("text_files"):
        os.makedirs("text_files")

def save_files(text, audio_filename, language):
    """
    텍스트를 오디오 파일과 텍스트 파일로 저장합니다.

    :param text: 변환할 텍스트
    :param audio_filename: 저장할 오디오 파일 이름 (확장자 포함)
    :param language: 변환할 텍스트의 언어 코드 (예: 'en', 'ko')
    :return: 오디오 파일 경로와 텍스트 파일 경로
    """
    # 오디오 파일 저장
    tts = gTTS(text=text, lang=language)
    audio_path = os.path.join("audio_files", audio_filename)
    tts.save(audio_path)

    # 텍스트 파일 저장
    text_filename = audio_filename.replace(".mp3", ".txt")
    text_path = os.path.join("text_files", text_filename)
    with open(text_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return audio_path, text_path

def main():
    """
    텍스트를 입력받아 오디오 파일과 텍스트 파일로 저장하는 메인 함수입니다.
    """
    ensure_directories()

    # 사용자로부터 텍스트 입력받기
    text = input("Enter the text to convert to speech: ")

    # 사용자로부터 파일 이름 입력받기
    filename = input("Enter the filename to save (without extension): ")
    audio_filename = f"{filename}.mp3"

    # 사용자로부터 언어 코드 입력받기 (기본값은 영어)
    language = input("Enter the language code (default is 'en'): ") or 'en'

    # 파일 저장
    audio_path, text_path = save_files(text, audio_filename, language)

    print(f"Files have been saved: \nAudio - {audio_path}\nText - {text_path}")

if __name__ == "__main__":
    main()
