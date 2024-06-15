import os
import tkinter as tk
from tkinter import messagebox
from gtts import gTTS

def ensure_directories():
    """
    오디오 파일과 텍스트 파일을 저장할 디렉토리가 존재하지 않으면 생성합니다.
    """
    if not os.path.exists("audio_files"):
        os.makedirs("audio_files")
    if not os.path.exists("text_files"):
        os.makedirs("text_files")

def save_files(text, audio_filename, language):
    """
    텍스트를 오디오 파일과 텍스트 파일로 저장합니다.

    :param text: 변환할 텍스트
    :param audio_filename: 저장할 오디오 파일 이름 (확장자 포함)
    :param language: 변환할 텍스트의 언어 코드 (예: 'en', 'ko')
    :return: 오디오 파일 경로와 텍스트 파일 경로
    """
    # 오디오 파일 저장
    tts = gTTS(text=text, lang=language)
    audio_path = os.path.join("audio_files", audio_filename)
    tts.save(audio_path)

    # 텍스트 파일 저장
    text_filename = audio_filename.replace(".mp3", ".txt")
    text_path = os.path.join("text_files", text_filename)
    with open(text_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return audio_path, text_path

def convert_and_save():
    """
    텍스트를 입력받아 오디오 파일과 텍스트 파일로 저장하는 함수입니다.
    """
    try:
        text = text_input.get("1.0", tk.END).strip()
        filename = filename_input.get().strip()
        language = language_input.get().strip() or 'en'

        if not text:
            status_label.config(text="텍스트를 입력하세요.")
            return

        if not filename:
            status_label.config(text="파일 이름을 입력하세요.")
            return

        audio_filename = f"{filename}.mp3"
        audio_path = os.path.join("audio_files", audio_filename)
        text_path = os.path.join("text_files", audio_filename.replace(".mp3", ".txt"))

        # 중복 파일 확인
        if os.path.exists(audio_path) or os.path.exists(text_path):
            messagebox.showerror("파일 중복", "이미 존재하는 파일입니다. 다른 파일 이름을 선택하세요.")
            return

        ensure_directories()
        audio_path, text_path = save_files(text, audio_filename, language)

        status_label.config(text=f"파일이 저장되었습니다: \n오디오 - {audio_path}\n텍스트 - {text_path}")
    except Exception as e:
        messagebox.showerror("오류", f"오류가 발생했습니다: {e}. 프로그램을 재시작합니다.")
        restart_program()

def restart_program():
    """
    프로그램을 재시작하는 함수입니다.
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)

# GUI 설정
app = tk.Tk()
app.title("텍스트를 음성 및 텍스트 파일로 저장")

tk.Label(app, text="변환할 텍스트를 입력하세요:").pack()
text_input = tk.Text(app, height=10, width=50)
text_input.pack()

tk.Label(app, text="저장할 파일 이름 (확장자 없이):").pack()
filename_input = tk.Entry(app)
filename_input.pack()

tk.Label(app, text="언어 코드 (기본값은 'en'):").pack()
language_input = tk.Entry(app)
language_input.pack()

convert_button = tk.Button(app, text="변환 및 저장", command=convert_and_save)
convert_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
