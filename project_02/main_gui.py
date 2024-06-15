import os
import tkinter as tk
from tkinter import filedialog, messagebox

# 파일 목록을 출력하는 함수
def list_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

# 파일 이름 변경 함수
def rename_file(directory, old_file, new_name):
    file_name, file_extension = os.path.splitext(old_file)
    new_file = os.path.join(directory, f"{new_name}{file_extension}")
    old_file_path = os.path.join(directory, old_file)
    os.rename(old_file_path, new_file)
    print(f"파일 이름 변경: {old_file_path} -> {new_file}")

# 디렉토리 선택 함수
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, directory)
        display_files(directory)

# 파일 목록 표시 함수
def display_files(directory):
    files = list_files(directory)
    listbox_files.delete(0, tk.END)
    for file in files:
        listbox_files.insert(tk.END, file)

# 파일 이름 변경 버튼 클릭 이벤트 핸들러
def on_rename_file():
    directory = entry_directory.get()
    if not directory:
        messagebox.showerror("오류", "디렉토리를 선택하세요.")
        return

    selected_file = listbox_files.get(tk.ACTIVE)
    if not selected_file:
        messagebox.showerror("오류", "파일을 선택하세요.")
        return

    new_name = entry_new_name.get()
    if not new_name:
        messagebox.showerror("오류", "새 파일명을 입력하세요.")
        return

    rename_file(directory, selected_file, new_name)
    display_files(directory)
    entry_new_name.delete(0, tk.END)
    messagebox.showinfo("성공", "파일 이름이 성공적으로 변경되었습니다.")

# GUI 설정
root = tk.Tk()
root.title("파일 이름 변경기")

tk.Label(root, text="디렉토리:").grid(row=0, column=0, padx=10, pady=5)
entry_directory = tk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="디렉토리 선택", command=select_directory).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="파일 목록:").grid(row=1, column=0, padx=10, pady=5)
listbox_files = tk.Listbox(root, width=50, height=15)
listbox_files.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

tk.Label(root, text="새 파일명:").grid(row=2, column=0, padx=10, pady=5)
entry_new_name = tk.Entry(root, width=50)
entry_new_name.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

tk.Button(root, text="파일 이름 변경", command=on_rename_file).grid(row=3, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()
