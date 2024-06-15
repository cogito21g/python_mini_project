import os
import shutil

def create_and_move_videos(directory):
    # 동영상 파일 확장자 리스트
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv']
    video_folder = os.path.join(directory, 'video_files')
    
    # video_files 디렉터리 생성
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
    
    # 현재 디렉터리 내의 동영상 파일 이동
    files = os.listdir(directory)
    for file in files:
        if os.path.isfile(os.path.join(directory, file)) and os.path.splitext(file)[1].lower() in video_extensions:
            shutil.move(os.path.join(directory, file), os.path.join(video_folder, file))
    
    return video_folder

def list_video_files(directory):
    files = os.listdir(directory)
    video_files = [f for f in files if os.path.splitext(f)[1].lower() in ['.mp4', '.avi', '.mov', '.mkv', '.flv']]
    return video_files

def rename_video_file(directory, file_name, new_name):
    old_path = os.path.join(directory, file_name)
    if os.path.isfile(old_path):
        extension = os.path.splitext(file_name)[1]
        new_file_name = f"{new_name}{extension}"
        new_path = os.path.join(directory, new_file_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{file_name}' to '{new_file_name}'")
    else:
        print(f"'{file_name}' is not a valid file.")

# 현재 디렉터리 설정
current_directory = os.getcwd()

# video_files 디렉터리 생성 및 파일 이동
video_folder = create_and_move_videos(current_directory)

# 동영상 파일 목록 표시
video_files = list_video_files(video_folder)
if not video_files:
    print("No video files found in the video_files directory.")
else:
    print("Video files in the video_files directory:")
    for index, file in enumerate(video_files, start=1):
        print(f"{index}. {file}")
    
    # 사용자에게 파일 선택 요청
    file_index = int(input("Enter the number of the file you want to rename: ")) - 1
    if 0 <= file_index < len(video_files):
        selected_file = video_files[file_index]
        new_name = input("Enter the new name for the video file (without extension): ")
        rename_video_file(video_folder, selected_file, new_name)
    else:
        print("Invalid file number selected.")
