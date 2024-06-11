import os
import tkinter as tk
from tkinter import messagebox

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

# 버튼 클릭 이벤트 핸들러
def on_create_files():
    directory = entry_directory.get()
    base_name = entry_base_name.get()
    try:
        num_files = int(entry_num_files.get())
    except ValueError:
        messagebox.showerror("입력 오류", "파일 개수는 숫자여야 합니다.")
        return
    extension = entry_extension.get()
    
    if not directory or not base_name or not extension:
        messagebox.showerror("입력 오류", "모든 필드를 입력해주세요.")
        return

    if os.path.exists(directory):
        messagebox.showerror("입력 오류", "폴더가 이미 존재합니다. 다른 이름을 입력해주세요.")
        return
    
    create_files(directory, base_name, num_files, extension)
    messagebox.showinfo("성공", f"{directory} 폴더에 {num_files}개의 {extension} 파일이 생성되었습니다.")
    root.destroy()

# GUI 설정
root = tk.Tk()
root.title("파일 생성기")

tk.Label(root, text="폴더 이름:").grid(row=0, column=0, padx=10, pady=5)
entry_directory = tk.Entry(root)
entry_directory.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="파일 기본 이름:").grid(row=1, column=0, padx=10, pady=5)
entry_base_name = tk.Entry(root)
entry_base_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="파일 개수:").grid(row=2, column=0, padx=10, pady=5)
entry_num_files = tk.Entry(root)
entry_num_files.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="파일 확장자:").grid(row=3, column=0, padx=10, pady=5)
entry_extension = tk.Entry(root)
entry_extension.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="파일 생성", command=on_create_files).grid(row=4, columnspan=2, pady=10)

root.mainloop()
