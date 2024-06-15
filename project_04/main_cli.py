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
    "exit"가 입력될 때까지 반복합니다. 예외 발생 시 재시작합니다.
    """
    ensure_directories()

    while True:
        try:
            # 사용자로부터 텍스트 입력받기
            text = input("변환할 텍스트를 입력하세요 (종료하려면 'exit' 입력): ").strip()
            if text.lower() == "exit":
                print("프로그램을 종료합니다.")
                break

            # 사용자로부터 언어 코드 입력받기 (기본값은 영어)
            language = input("언어 코드를 입력하세요 (기본값은 'en'): ").strip() or 'en'

            while True:
                # 사용자로부터 파일 이름 입력받기
                filename = input("저장할 파일 이름을 입력하세요 (확장자 없이): ").strip()
                if not filename:
                    print("파일 이름을 입력하세요.")
                    continue

                audio_filename = f"{filename}.mp3"
                audio_path = os.path.join("audio_files", audio_filename)
                text_path = os.path.join("text_files", audio_filename.replace(".mp3", ".txt"))

                # 중복 파일 확인
                if os.path.exists(audio_path) or os.path.exists(text_path):
                    print("이미 존재하는 파일입니다. 다른 파일 이름을 선택하세요.")
                    continue

                # 파일 저장
                audio_path, text_path = save_files(text, audio_filename, language)
                print(f"파일이 저장되었습니다: \n오디오 - {audio_path}\n텍스트 - {text_path}")
                break

        except Exception as e:
            print(f"오류가 발생했습니다: {e}. 프로그램을 재시작합니다.")

if __name__ == "__main__":
    main()
