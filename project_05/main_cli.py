from gtts import gTTS
import os
import pygame

def text_to_speech(text_file, output_file):
    # 텍스트 파일을 읽습니다
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # 파일이 이미 존재하는지 확인합니다
    if os.path.exists(output_file):
        print(f"Error: The file '{output_file}' already exists.")
    else:
        # gTTS 객체를 생성하여 텍스트를 음성으로 변환합니다 (기본 언어는 영어)
        tts = gTTS(text=text, lang='en')
        
        # 변환된 음성을 파일로 저장합니다
        tts.save(output_file)
        
        # pygame 초기화
        pygame.mixer.init()
        
        # 저장된 파일을 재생합니다
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        # 음성 파일이 끝날 때까지 대기합니다
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

# 예제 사용법
text_file = 'example.txt'  # 변환할 텍스트 파일의 경로
output_file = input("Enter the output file name (with .mp3 extension): ")  # 출력할 음성 파일의 이름을 입력받습니다

text_to_speech(text_file, output_file)
