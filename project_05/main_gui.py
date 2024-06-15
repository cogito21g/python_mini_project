import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QLabel, QMessageBox
from gtts import gTTS

class TextToSpeechApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text to Speech Converter')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Select a text file from the list below (or type "exit" to quit):', self)
        layout.addWidget(self.label)

        self.text_file_btn = QPushButton('Select Text File', self)
        self.text_file_btn.clicked.connect(self.select_text_file)
        layout.addWidget(self.text_file_btn)

        self.output_name_label = QLabel('Enter output file name (default is "output"):', self)
        layout.addWidget(self.output_name_label)

        self.output_name_input = QLineEdit(self)
        layout.addWidget(self.output_name_input)

        self.convert_btn = QPushButton('Convert to Speech', self)
        self.convert_btn.clicked.connect(self.convert_to_speech)
        layout.addWidget(self.convert_btn)

        self.setLayout(layout)

        # 디렉토리 생성
        os.makedirs('text_files', exist_ok=True)
        os.makedirs('audio_files', exist_ok=True)

        # 텍스트 파일을 text_files 폴더로 이동
        text_files = [f for f in os.listdir() if f.endswith('.txt')]
        for text_file in text_files:
            shutil.move(text_file, os.path.join('text_files', text_file))

        self.text_file_path = None

    def select_text_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Text File", "text_files", "Text Files (*.txt)", options=options)
        if file_name:
            self.text_file_path = file_name
            self.label.setText(f'Selected File: {os.path.basename(file_name)}')

    def convert_to_speech(self):
        if not self.text_file_path:
            QMessageBox.warning(self, "Warning", "Please select a text file first!")
            return

        output_file_name = self.output_name_input.text() or "output"
        output_file = os.path.join('audio_files', f"{output_file_name}.mp3")

        if os.path.exists(output_file):
            QMessageBox.warning(self, "Warning", f"The file '{output_file}' already exists. Please choose a different name.")
        else:
            try:
                self.text_to_speech(self.text_file_path, output_file)
                QMessageBox.information(self, "Success", f"Audio file '{output_file}' has been created.")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def text_to_speech(self, text_file, output_file):
        # 텍스트 파일을 읽습니다
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # gTTS 객체를 생성하여 텍스트를 음성으로 변환합니다 (기본 언어는 영어)
        tts = gTTS(text=text, lang='en')
        
        # 변환된 음성을 파일로 저장합니다
        tts.save(output_file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextToSpeechApp()
    ex.show()
    sys.exit(app.exec_())
