import os

# 폴더 생성 함수
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# 파일 생성 함수
def create_markdown_files(directory, base_name, num_files):
    create_directory(directory)
    for i in range(1, num_files + 1):
        file_name = os.path.join(directory, f"{base_name}_{i}.md")
        with open(file_name, "w") as file:
            file.write(f"# 파일 {i}\n")
            file.write(f"이것은 파일 {i}의 내용입니다.\n")

# 사용자 입력 받기
directory = "progress"
base_name = input("생성할 파일의 기본 이름을 입력하세요: ")
num_files = int(input("생성할 파일의 개수를 입력하세요: "))

create_markdown_files(directory, base_name, num_files)

print(f"{directory} 폴더에 {num_files}개의 Markdown 파일이 생성되었습니다.")
