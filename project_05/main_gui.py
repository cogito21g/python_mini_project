import sys
import os
import shutil
from datetime import datetime
from gtts import gTTS
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QLabel, QMessageBox

def text_to_speech(text_file, output_file):
    """
    텍스트 파일을 음성 파일로 변환합니다.
    
    :param text_file: 변환할 텍스트 파일의 경로
    :param output_file: 저장할 음성 파일의 경로
    """
    # 텍스트 파일을 읽습니다
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # gTTS 객체를 생성하여 텍스트를 음성으로 변환합니다 (기본 언어는 영어)
    tts = gTTS(text=text, lang='en')
    
    # 변환된 음성을 파일로 저장합니다
    tts.save(output_file)
    
    # 로그 기록
    log_message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Converted '{text_file}' to '{output_file}'\n"
    log(log_message)

def log(message):
    """
    로그 메시지를 날짜별로 기록합니다.
    
    :param message: 로그에 기록할 메시지
    """
    # log 폴더 생성
    os.makedirs('log', exist_ok=True)
    
    # 날짜별 로그 파일 이름 생성
    log_file_name = datetime.now().strftime("log/%Y-%m-%d.log")
    
    # 로그 메시지 파일에 추가
    with open(log_file_name, 'a', encoding='utf-8') as log_file:
        log_file.write(message)

class TextToSpeechApp(QWidget):
    def __init__(self):
        super().__init__()

        # UI 초기화
        self.initUI()

    def initUI(self):
        """
        GUI를 초기화하고 구성 요소를 설정합니다.
        """
        self.setWindowTitle('Text to Speech Converter')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # 파일 선택 라벨
        self.label = QLabel('Select a text file from the list below:', self)
        layout.addWidget(self.label)

        # 파일 선택 버튼
        self.text_file_btn = QPushButton('Select Text File', self)
        self.text_file_btn.clicked.connect(self.select_text_file)
        layout.addWidget(self.text_file_btn)

        # 출력 파일명 입력 라벨
        self.output_name_label = QLabel('Enter output file name (default is "output"):', self)
        layout.addWidget(self.output_name_label)

        # 출력 파일명 입력 필드
        self.output_name_input = QLineEdit(self)
        layout.addWidget(self.output_name_input)

        # 변환 버튼
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
        """
        파일 선택 다이얼로그를 표시하고 사용자가 선택한 파일 경로를 저장합니다.
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Text File", "text_files", "Text Files (*.txt)", options=options)
        if file_name:
            self.text_file_path = file_name
            self.label.setText(f'Selected File: {os.path.basename(file_name)}')

    def convert_to_speech(self):
        """
        선택한 텍스트 파일을 음성 파일로 변환합니다.
        """
        if not self.text_file_path:
            QMessageBox.warning(self, "Warning", "Please select a text file first!")
            return

        output_file_name = self.output_name_input.text() or "output"
        output_file = os.path.join('audio_files', f"{output_file_name}.mp3")

        if os.path.exists(output_file):
            QMessageBox.warning(self, "Warning", f"The file '{output_file}' already exists. Please choose a different name.")
        else:
            try:
                text_to_speech(self.text_file_path, output_file)
                QMessageBox.information(self, "Success", f"Audio file '{output_file}' has been created.")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    # 애플리케이션 실행
    app = QApplication(sys.argv)
    ex = TextToSpeechApp()
    ex.show()
    sys.exit(app.exec_())
