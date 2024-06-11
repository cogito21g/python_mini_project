import os

# 폴더 생성 함수
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    return False

# 파일 생성 함수
def create_files(directory, base_name, num_files, extension):
    create_directory(directory)
    for i in range(1, num_files + 1):
        file_name = os.path.join(directory, f"{base_name}_{i}.{extension}")
        with open(file_name, "w") as file:
            file.write(f"# 파일 {i}\n")
            file.write(f"이것은 파일 {i}의 내용입니다.\n")

# 사용자 입력 받기
while True:
    directory = input("생성할 폴더 이름을 입력하세요: ")
    if create_directory(directory):
        break
    else:
        print("이미 존재하는 폴더입니다. 다른 이름을 입력해주세요.")

base_name = input("생성할 파일의 기본 이름을 입력하세요: ")
num_files = int(input("생성할 파일의 개수를 입력하세요: "))
extension = input("생성할 파일의 확장자를 입력하세요 (예: md, txt 등): ")

create_files(directory, base_name, num_files, extension)

print(f"{directory} 폴더에 {num_files}개의 {extension} 파일이 생성되었습니다.")
