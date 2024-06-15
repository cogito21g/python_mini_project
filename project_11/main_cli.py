import os
import datetime

def rename_video_files(directory):
    # 동영상 파일 확장자 리스트
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv']

    # 디렉터리 내의 파일 목록을 가져옴
    files = os.listdir(directory)

    # 동영상 파일만 필터링
    video_files = [f for f in files if os.path.splitext(f)[1].lower() in video_extensions]

    for index, file in enumerate(video_files):
        # 기존 파일 경로
        old_path = os.path.join(directory, file)
        
        # 새로운 파일명 생성 (예: video_20230615_01.mp4)
        new_file_name = f"video_{datetime.datetime.now().strftime('%Y%m%d')}_{index + 1}{os.path.splitext(file)[1]}"
        new_path = os.path.join(directory, new_file_name)
        
        # 파일명 변경
        os.rename(old_path, new_path)
        print(f"Renamed '{file}' to '{new_file_name}'")

# 사용 예시
rename_video_files('./')
