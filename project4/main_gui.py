import os
from gtts import gTTS
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QFileDialog

class TextToSpeechApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Text to Speech Converter")

        self.layout = QVBoxLayout()

        self.text_label = QLabel("Enter text to be converted to speech:")
        self.layout.addWidget(self.text_label)

        self.text_input = QTextEdit()
        self.layout.addWidget(self.text_input)

        self.filename_label = QLabel("Enter filename:")
        self.layout.addWidget(self.filename_label)

        self.filename_input = QLineEdit()
        self.layout.addWidget(self.filename_input)

        self.load_button = QPushButton("Load Text from File")
        self.load_button.clicked.connect(self.load_text_from_file)
        self.layout.addWidget(self.load_button)

        self.submit_button = QPushButton("Convert to Speech")
        self.submit_button.clicked.connect(self.on_submit)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

        # Set tab order
        self.setTabOrder(self.text_input, self.filename_input)
        self.setTabOrder(self.filename_input, self.load_button)
        self.setTabOrder(self.load_button, self.submit_button)

        # Enter key triggers the submit action
        self.filename_input.returnPressed.connect(self.on_submit)
        self.text_input.textChanged.connect(self.on_text_change)

    def load_text_from_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt)", options=options)
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.text_input.setPlainText(file_content)

    def save_audio_file(self, text, folder='audio_files', filename='output'):
        # 폴더가 없다면 생성
        if not os.path.exists(folder):
            os.makedirs(folder)

        file_path = os.path.join(folder, f"{filename}.mp3")

        # 동일한 파일이 있는지 확인
        if os.path.exists(file_path):
            return False

        # 텍스트를 음성으로 변환하여 파일로 저장
        tts = gTTS(text=text, lang='en')
        tts.save(file_path)

        return True

    def on_submit(self):
        text = self.text_input.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Input Error", "Please enter some text.")
            return

        filename = self.filename_input.text().strip()
        if not filename:
            QMessageBox.warning(self, "Input Error", "Please enter a filename.")
            return

        if not self.save_audio_file(text, filename=filename):
            QMessageBox.warning(self, "File Error", f"A file named '{filename}.mp3' already exists. Please enter a different filename.")
        else:
            QMessageBox.information(self, "Success", f"Audio file has been saved as 'audio_files/{filename}.mp3'.")

    def on_text_change(self):
        self.text_input.setTabChangesFocus(True)

if __name__ == '__main__':
    app = QApplication([])
    ex = TextToSpeechApp()
    ex.show()
    app.exec_()
