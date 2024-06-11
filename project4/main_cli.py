import os
from gtts import gTTS

def save_audio_file(text, folder='audio_files', filename='output'):
    """
    텍스트를 음성 파일로 변환하여 저장하는 함수.
    중복된 파일명이 있을 경우 숫자를 붙여서 파일명을 변경합니다.

    :param text: 변환할 텍스트
    :param folder: 음성 파일을 저장할 폴더
    :param filename: 저장할 파일의 기본 이름
    """
    # 폴더가 없다면 생성
    if not os.path.exists(folder):
        os.makedirs(folder)

    # 파일 이름 결정
    base_filename = filename
    file_path = os.path.join(folder, f"{base_filename}.mp3")
    count = 1

    # 중복된 파일이 있다면 숫자를 붙여줌
    while os.path.exists(file_path):
        file_path = os.path.join(folder, f"{base_filename}_{count}.mp3")
        count += 1

    # 텍스트를 음성으로 변환하여 파일로 저장
    tts = gTTS(text=text, lang='en')
    tts.save(file_path)

    print(f"Audio file has been saved as '{file_path}'.")

def list_text_files(directory):
    """
    주어진 디렉토리에서 텍스트 파일 리스트를 반환하는 함수.

    :param directory: 탐색할 디렉토리
    :return: 텍스트 파일 리스트
    """
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

def main():
    while True:
        # 사용자로부터 텍스트 입력 방법 선택
        print("Choose an option:")
        print("1. Enter text manually")
        print("2. Load text from a file")
        print("Type 'exit' to quit at any time.")
        choice = input("Enter your choice (1/2/exit): ")

        if choice.lower() == 'exit':
            print("Exiting the program.")
            break

        if choice == '1':
            # 사용자로부터 텍스트 입력 받기
            text = input("Enter the text to be converted to speech (or type 'exit' to quit): ")
            if text.lower() == 'exit':
                print("Exiting the program.")
                break
        elif choice == '2':
            # 디렉토리 입력 받기
            directory = input("Enter the directory to search for text files (or type 'exit' to quit): ")
            if directory.lower() == 'exit':
                print("Exiting the program.")
                break
            if not os.path.exists(directory):
                print("Directory does not exist. Please try again.")
                continue

            # 텍스트 파일 리스트 가져오기
            text_files = list_text_files(directory)
            if not text_files:
                print("No text files found in the directory. Please try again.")
                continue

            # 텍스트 파일 리스트 표시
            print("Select a text file to load:")
            for idx, file in enumerate(text_files):
                print(f"{idx + 1}. {file}")
            file_choice = input("Enter the number of the file to load (or type 'exit' to quit): ")

            if file_choice.lower() == 'exit':
                print("Exiting the program.")
                break

            if not file_choice.isdigit() or int(file_choice) < 1 or int(file_choice) > len(text_files):
                print("Invalid choice. Please try again.")
                continue

            # 선택한 파일 경로
            selected_file = text_files[int(file_choice) - 1]
            file_path = os.path.join(directory, selected_file)

            # 텍스트 파일에서 내용 읽기
            with open(file_path, 'r') as file:
                text = file.read()
        else:
            print("Invalid choice. Please try again.")
            continue

        # 사용자로부터 파일 이름 입력 받기 (기본값은 'output')
        user_filename = input("Enter the filename (default is 'output', or type 'exit' to quit): ") or 'output'
        if user_filename.lower() == 'exit':
            print("Exiting the program.")
            break

        # 파일 저장 함수 호출
        save_audio_file(text, filename=user_filename)

if __name__ == '__main__':
    main()
