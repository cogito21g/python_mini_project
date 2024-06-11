import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# 파일 목록을 출력하는 함수
def list_files(directory):
    # 이미지 파일 확장자 목록
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and os.path.splitext(f)[1].lower() in image_extensions]
    return files

# 파일 이름 변경 함수
def rename_file(directory, old_file, new_name):
    old_file_path = os.path.join(directory, old_file)
    file_name, file_extension = os.path.splitext(old_file)
    new_file_path = os.path.join(directory, f"{new_name}{file_extension}")
    
    if os.path.exists(new_file_path):
        messagebox.showerror("오류", "같은 이름의 파일이 이미 존재합니다. 다른 이름을 입력하세요.")
        return False
    
    os.rename(old_file_path, new_file_path)
    print(f"파일 이름 변경: {old_file_path} -> {new_file_path}")
    return True

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

# 파일 선택 이벤트 핸들러
def on_file_select(event):
    selected_file = listbox_files.get(tk.ACTIVE)
    display_image(selected_file)

# 이미지 표시 함수
def display_image(file_name):
    directory = entry_directory.get()
    file_path = os.path.join(directory, file_name)
    
    # 이미지 캐싱을 위해 전역 이미지 캐시 사용
    if file_path not in image_cache:
        image = Image.open(file_path)
        image.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(image)
        image_cache[file_path] = photo
    else:
        photo = image_cache[file_path]

    label_image.config(image=photo)
    label_image.image = photo

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

    if rename_file(directory, selected_file, new_name):
        display_files(directory)
        entry_new_name.delete(0, tk.END)
        messagebox.showinfo("성공", "파일 이름이 성공적으로 변경되었습니다.")

# 전역 이미지 캐시 딕셔너리
image_cache = {}

# GUI 설정
root = tk.Tk()
root.title("이미지 파일 이름 변경기")

tk.Label(root, text="디렉토리:").grid(row=0, column=0, padx=10, pady=5)
entry_directory = tk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="디렉토리 선택", command=select_directory).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="파일 목록:").grid(row=1, column=0, padx=10, pady=5)
listbox_files = tk.Listbox(root, width=50, height=15)
listbox_files.grid(row=1, column=1, padx=10, pady=5, columnspan=2)
listbox_files.bind("<<ListboxSelect>>", on_file_select)

label_image = tk.Label(root)
label_image.grid(row=1, column=3, padx=10, pady=5)

tk.Label(root, text="새 파일명:").grid(row=2, column=0, padx=10, pady=5)
entry_new_name = tk.Entry(root, width=50)
entry_new_name.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

tk.Button(root, text="파일 이름 변경", command=on_rename_file).grid(row=3, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()
