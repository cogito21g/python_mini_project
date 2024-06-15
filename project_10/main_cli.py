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

def rename_audio_files(directory, new_name):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")
    
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
                else:
                    print("Invalid number. Please try again.")
            else:
                if selection in mp3_files:
                    file_path = os.path.join(directory, selection)
                    stop_playback_func()  # 이전 재생 중지
                    play_audio(file_path)
                else:
                    print("Invalid name. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    for filename in mp3_files:
        file_path = os.path.join(directory, filename)
        base, ext = os.path.splitext(filename)
        new_filename = f"{new_name}_{base}{ext}"
        new_file_path = os.path.join(directory, new_filename)
        os.rename(file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")

# 디렉토리 경로와 새 파일명을 지정합니다.
directory = 'audio_files'
new_name = 'new_audio_name'

rename_audio_files(directory, new_name)
