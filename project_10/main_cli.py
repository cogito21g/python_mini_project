import os
import threading
import pygame
import time

# 초기화
pygame.mixer.init()

# 글로벌 변수와 잠금을 사용하여 스레드 간의 동기화 처리
stop_playback = False
playback_thread = None
playback_lock = threading.Lock()

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_playback_func():
    pygame.mixer.music.stop()

def rename_audio_files(directory, new_name, text_directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")
    
    if not os.path.exists(text_directory):
        os.makedirs(text_directory)
        print(f"Directory {text_directory} created.")
    
    mp3_files = [f for f in os.listdir(directory) if f.endswith(".mp3")]
    
    if not mp3_files:
        print(f"No .mp3 files found in directory {directory}.")
        return
    
    print(f"Found {len(mp3_files)} .mp3 file(s) in directory {directory}:")
    for idx, filename in enumerate(mp3_files, 1):
        print(f"{idx}. {filename}")
    
    while True:
        selection = input("Enter the number or name of the file you want to play (or 'q' to quit, 's' to stop): ").strip()
        
        if selection.lower() == 'q':
            stop_playback_func()
            break
        
        if selection.lower() == 's':
            stop_playback_func()
            continue
        
        try:
            if selection.isdigit():
                index = int(selection) - 1
                if 0 <= index < len(mp3_files):
                    file_path = os.path.join(directory, mp3_files[index])
                    stop_playback_func()  # 이전 재생 중지
                    play_audio(file_path)
                    new_filename = input(f"Enter the new name for {mp3_files[index]}: ").strip() + ".mp3"
                    new_file_path = os.path.join(directory, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {mp3_files[index]} to {new_filename}")
                    write_info_file(text_directory, new_filename)
                else:
                    print("Invalid number. Please try again.")
            else:
                if selection in mp3_files:
                    file_path = os.path.join(directory, selection)
                    stop_playback_func()  # 이전 재생 중지
                    play_audio(file_path)
                    new_filename = input(f"Enter the new name for {selection}: ").strip() + ".mp3"
                    new_file_path = os.path.join(directory, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {selection} to {new_filename}")
                    write_info_file(text_directory, new_filename)
                else:
                    print("Invalid name. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
def write_info_file(text_directory, new_filename):
    text_file_path = os.path.join(text_directory, os.path.splitext(new_filename)[0] + ".txt")
    with open(text_file_path, "w") as file:
        file.write(f"File {new_filename} was renamed and stored in the directory.\n")
    print(f"Information written to {text_file_path}")

# 디렉토리 경로와 새 파일명을 지정합니다.
audio_directory = 'audio_files'
new_name = 'new_audio_name'
text_directory = 'text_files'

rename_audio_files(audio_directory, new_name, text_directory)
