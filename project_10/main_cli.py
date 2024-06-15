import os
from pydub import AudioSegment
from pydub.playback import play

def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)

def rename_audio_files(directory, new_name):
    # 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")
    
    # 디렉토리 내의 모든 파일에 대해 반복
    mp3_files = [f for f in os.listdir(directory) if f.endswith(".mp3")]
    
    if not mp3_files:
        print(f"No .mp3 files found in directory {directory}.")
        return
    
    print(f"Found {len(mp3_files)} .mp3 file(s) in directory {directory}:")
    for idx, filename in enumerate(mp3_files, 1):
        print(f"{idx}. {filename}")
    
    while True:
        selection = input("Enter the number or name of the file you want to play (or 'q' to quit): ").strip()
        
        if selection.lower() == 'q':
            break
        
        try:
            # 사용자가 번호를 입력한 경우
            if selection.isdigit():
                index = int(selection) - 1
                if 0 <= index < len(mp3_files):
                    file_path = os.path.join(directory, mp3_files[index])
                    play_audio(file_path)
                else:
                    print("Invalid number. Please try again.")
            else:
                # 사용자가 파일 이름을 입력한 경우
                if selection in mp3_files:
                    file_path = os.path.join(directory, selection)
                    play_audio(file_path)
                else:
                    print("Invalid name. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    for filename in mp3_files:
        file_path = os.path.join(directory, filename)
        
        # 파일명 변경
        base, ext = os.path.splitext(filename)
        new_filename = f"{new_name}_{base}{ext}"
        new_file_path = os.path.join(directory, new_filename)
        
        os.rename(file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")

# 디렉토리 경로와 새 파일명을 지정합니다.
directory = 'audio_files'
new_name = 'new_audio_name'

rename_audio_files(directory, new_name)
