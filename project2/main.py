import os

# 파일 목록을 출력하는 함수
def list_files(directory):
    # 디렉토리 내의 모든 파일 목록을 출력
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print(f"{directory} 디렉토리 내의 파일 목록:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}: {file}")
    return files

# 파일 이름 변경 함수
def rename_file(directory, file, new_name):
    old_file = os.path.join(directory, file)
    new_file = os.path.join(directory, new_name)
    os.rename(old_file, new_file)
    print(f"파일 이름 변경: {old_file} -> {new_file}")

# 사용자 입력 받기
directory = input("파일이 위치한 디렉토리 경로를 입력하세요: ")

# 디렉토리 내의 파일 목록을 출력
files = list_files(directory)

if files:
    # 파일 선택
    file_index = int(input("이름을 변경할 파일의 번호를 선택하세요: ")) - 1
    if 0 <= file_index < len(files):
        selected_file = files[file_index]
        new_name = input(f"새로운 파일명을 입력하세요: ")
        
        # 파일 이름 변경 함수 호출
        rename_file(directory, selected_file, new_name)
    else:
        print("유효한 파일 번호를 선택하세요.")
else:
    print("변경할 수 있는 파일이 없습니다.")
