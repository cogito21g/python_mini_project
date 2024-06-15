from gtts import gTTS
import os
import shutil

def text_to_speech(text_file, output_file):
    # 텍스트 파일을 읽습니다
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # gTTS 객체를 생성하여 텍스트를 음성으로 변환합니다 (기본 언어는 영어)
    tts = gTTS(text=text, lang='en')
    
    # 변환된 음성을 파일로 저장합니다
    tts.save(output_file)

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
        print("Select a text file from the list below (or type 'exit' to quit):")
        text_files_list = os.listdir('text_files')
        for idx, file in enumerate(text_files_list, 1):
            print(f"{idx}. {file}")

        file_choice = input("Enter the number or name of the file you want to convert to speech: ")

        if file_choice.lower() == "exit":
            print("Exiting program.")
            break

        if file_choice.isdigit():
            file_choice = int(file_choice) - 1
            if file_choice not in range(len(text_files_list)):
                print("Invalid choice. Please try again.")
                continue
            selected_file = text_files_list[file_choice]
        else:
            if file_choice not in text_files_list:
                print("Invalid choice. Please try again.")
                continue
            selected_file = file_choice

        text_file_path = os.path.join('text_files', selected_file)

        while True:
            # 음성 파일의 이름을 입력받고 기본 이름 설정
            output_file_name = input("Enter the output file name (without extension, default is 'output', type 'exit' to quit): ") or "output"
            
            if output_file_name.lower() == "exit":
                print("Exiting program.")
                return
            
            output_file = os.path.join('audio_files', f"{output_file_name}.mp3")

            if os.path.exists(output_file):
                print(f"Error: The file '{output_file}' already exists. Please choose a different name.")
            else:
                # 음성 변환 및 저장
                text_to_speech(text_file_path, output_file)
                print(f"Audio file '{output_file}' has been created.")
                break

if __name__ == "__main__":
    main()
