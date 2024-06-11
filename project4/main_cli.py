import os
from gtts import gTTS

def save_audio_file(text, folder='audio_files', filename='output'):
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

# 사용자로부터 텍스트 입력 받기
text = input("Enter the text to be converted to speech: ")

# 사용자로부터 파일 이름 입력 받기 (기본값은 'output')
user_filename = input("Enter the filename (default is 'output'): ") or 'output'

# 파일 저장 함수 호출
save_audio_file(text, filename=user_filename)
