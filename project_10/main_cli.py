import os
import pygame
from datetime import datetime

# pygame 초기화
pygame.mixer.init()

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_playback_func():
    pygame.mixer.music.stop()

def rename_audio_files(directory, text_directory, log_directory):
    # 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")
    
    # 텍스트 파일 디렉토리가 없으면 생성
    if not os.path.exists(text_directory):
        os.makedirs(text_directory)
        print(f"Directory {text_directory} created.")
    
    # 로그 파일 디렉토리가 없으면 생성
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        print(f"Directory {log_directory} created.")
    
    # .mp3 파일 목록을 가져옴
    mp3_files = [f for f in os.listdir(directory) if f.endswith(".mp3")]
    
    if not mp3_files:
        print(f"No .mp3 files found in directory {directory}.")
        return
    
    # 파일 목록 출력
    print(f"Found {len(mp3_files)} .mp3 file(s) in directory {directory}:")
    for idx, filename in enumerate(mp3_files, 1):
        print(f"{idx}. {filename}")
    
    while True:
        selection = input("Enter the number or name of the file you want to play (or 'q' to quit, 's' to stop): ").strip()
        
        if selection.lower() == 'q':  # 종료
            stop_playback_func()
            break
        
        if selection.lower() == 's':  # 재생 중지
            stop_playback_func()
            continue
        
        try:
            if selection.isdigit():  # 번호로 파일 선택
                index = int(selection) - 1
                if 0 <= index < len(mp3_files):
                    file_path = os.path.join(directory, mp3_files[index])
                    stop_playback_func()  # 이전 재생 중지
                    play_audio(file_path)
                    new_filename = input(f"Enter the new name for {mp3_files[index]} (without extension): ").strip() + ".mp3"
                    new_file_path = os.path.join(directory, new_filename)
                    if os.path.exists(new_file_path):  # 파일명 중복 확인
                        print(f"File {new_filename} already exists. Choose a different name.")
                        continue
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {mp3_files[index]} to {new_filename}")
                    text_info = input("Enter the information to be saved in the text file: ").strip()
                    write_info_file(text_directory, new_filename, text_info)
                    write_log_file(log_directory, f"Renamed {mp3_files[index]} to {new_filename}")
                else:
                    print("Invalid number. Please try again.")
            else:  # 이름으로 파일 선택
                if selection in mp3_files:
                    file_path = os.path.join(directory, selection)
                    stop_playback_func()  # 이전 재생 중지
                    play_audio(file_path)
                    new_filename = input(f"Enter the new name for {selection} (without extension): ").strip() + ".mp3"
                    new_file_path = os.path.join(directory, new_filename)
                    if os.path.exists(new_file_path):  # 파일명 중복 확인
                        print(f"File {new_filename} already exists. Choose a different name.")
                        continue
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {selection} to {new_filename}")
                    text_info = input("Enter the information to be saved in the text file: ").strip()
                    write_info_file(text_directory, new_filename, text_info)
                    write_log_file(log_directory, f"Renamed {selection} to {new_filename}")
                else:
                    print("Invalid name. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

# 텍스트 파일에 정보를 기록하는 함수
def write_info_file(text_directory, new_filename, text_info):
    text_file_path = os.path.join(text_directory, os.path.splitext(new_filename)[0] + ".txt")
    with open(text_file_path, "w") as file:
        file.write(text_info)
    print(f"Information written to {text_file_path}")

# 로그 파일에 기록하는 함수
def write_log_file(log_directory, log_info):
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file_path = os.path.join(log_directory, f"log_{date_str}.txt")
    with open(log_file_path, "a") as log_file:  # 'a' 모드로 열어 내용을 추가
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {log_info}\n")
    print(f"Log entry added to {log_file_path}")

# 디렉토리 경로를 지정합니다.
audio_directory = 'audio_files'
text_directory = 'text_files'
log_directory = 'log_files'

# 파일명 변경 함수 호출
rename_audio_files(audio_directory, text_directory, log_directory)
