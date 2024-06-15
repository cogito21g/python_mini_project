import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import os

def convert_text_to_speech():
    text = text_input.get("1.0", tk.END)
    tts = gTTS(text=text, lang='ko')
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if save_path:
        tts.save(save_path)
        status_label.config(text="파일이 저장되었습니다: " + save_path)

# GUI 설정
app = tk.Tk()
app.title("텍스트를 음성으로 변환")

text_input = tk.Text(app, height=10, width=50)
text_input.pack()

convert_button = tk.Button(app, text="변환", command=convert_text_to_speech)
convert_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
