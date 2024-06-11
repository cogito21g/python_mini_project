import os

# 파일 생성 함수
def create_markdown_files(num_files):
    for i in range(1, num_files + 1):
        file_name = f"file{i}.md"
        with open(file_name, "w") as file:
            file.write(f"# 파일 {i}\n")
            file.write(f"이것은 파일 {i}의 내용입니다.\n")

# 20개의 markdown 파일 생성
create_markdown_files(20)

print("20개의 Markdown 파일이 생성되었습니다.")
