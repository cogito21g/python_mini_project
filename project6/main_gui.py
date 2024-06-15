import sys
import os
import shutil
import io
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QListWidget, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QProgressDialog
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import speech_recognition as sr
from pydub import AudioSegment

class Worker(QThread):
    progress = pyqtSignal(str)

    def __init__(self, audio_file_path, log_file_path):
        super().__init__()
        self.audio_file_path = audio_file_path
        self.log_file_path = log_file_path

    def run(self):
        recognizer = sr.Recognizer()
        file_extension = os.path.splitext(self.audio_file_path)[1].lower()
        file_name = os.path.splitext(os.path.basename(self.audio_file_path))[0]
        text_file_path = f"text_files/{file_name}.txt"

        with open(self.log_file_path, 'a', encoding='utf-8') as log_file:
            if os.path.exists(text_file_path):
                log_file.write(f"{datetime.now()} - {self.audio_file_path} - 이미 존재함\n")
                self.progress.emit(f"{text_file_path} 이미 존재합니다. 변환을 건너뜁니다.")
                return

            if file_extension == '.mp3':
                audio = AudioSegment.from_mp3(self.audio_file_path)
                wav_io = io.BytesIO()
                audio.export(wav_io, format='wav')
                wav_io.seek(0)
                audio_file = wav_io
            elif file_extension == '.wav':
                audio_file = self.audio_file_path
            else:
                log_file.write(f"{datetime.now()} - {self.audio_file_path} - 지원되지 않는 파일 형식\n")
                self.progress.emit("지원되지 않는 파일 형식입니다.")
                return

            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_data, language='ko-KR')
                    with open(text_file_path, 'w', encoding='utf-8') as text_file:
                        text_file.write(text)
                    log_file.write(f"{datetime.now()} - {self.audio_file_path} - 변환 성공\n")
                    self.progress.emit(f"텍스트가 파일로 저장되었습니다: {text_file_path}")
                except sr.UnknownValueError:
                    log_file.write(f"{datetime.now()} - {self.audio_file_path} - 음성을 인식할 수 없음\n")
                    self.progress.emit("음성을 인식할 수 없습니다.")
                except sr.RequestError as e:
                    log_file.write(f"{datetime.now()} - {self.audio_file_path} - API 요청 에러: {e}\n")
                    self.progress.emit(f"API 요청 에러: {e}")
                finally:
                    if isinstance(audio_file, io.BytesIO):
                        audio_file.close()

class AudioToTextApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Audio to Text Converter")
        self.setGeometry(100, 100, 800, 400)

        self.create_folders()
        self.move_audio_files_to_folder()

        self.layout = QHBoxLayout()

        self.audio_files_layout = QVBoxLayout()
        self.audio_files_label = QLabel("audio_files 폴더 내의 파일 목록:")
        self.audio_files_layout.addWidget(self.audio_files_label)

        self.audio_file_list = QListWidget()
        self.update_audio_file_list()
        self.audio_files_layout.addWidget(self.audio_file_list)

        self.convert_button = QPushButton("변환")
        self.convert_button.clicked.connect(self.convert_selected_file)
        self.audio_files_layout.addWidget(self.convert_button)

        self.layout.addLayout(self.audio_files_layout)

        self.text_files_layout = QVBoxLayout()
        self.text_files_label = QLabel("변환된 텍스트 파일 목록:")
        self.text_files_layout.addWidget(self.text_files_label)

        self.text_file_list = QListWidget()
        self.update_text_file_list()
        self.text_files_layout.addWidget(self.text_file_list)

        self.layout.addLayout(self.text_files_layout)

        self.exit_button = QPushButton("종료")
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def create_folders(self):
        if not os.path.exists('audio_files'):
            os.makedirs('audio_files')
        if not os.path.exists('text_files'):
            os.makedirs('text_files')
        if not os.path.exists('logs'):
            os.makedirs('logs')

    def move_audio_files_to_folder(self):
        audio_extensions = ['.mp3', '.wav']
        for file in os.listdir('.'):
            if os.path.isfile(file) and os.path.splitext(file)[1].lower() in audio_extensions:
                shutil.move(file, f"audio_files/{file}")

    def update_audio_file_list(self):
        self.audio_file_list.clear()
        files = os.listdir('audio_files')
        for file in files:
            self.audio_file_list.addItem(file)

    def update_text_file_list(self):
        self.text_file_list.clear()
        files = os.listdir('text_files')
        for file in files:
            self.text_file_list.addItem(file)

    def convert_selected_file(self):
        selected_items = self.audio_file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "파일을 선택하세요")
            return

        audio_file_name = selected_items[0].text()
        audio_file_path = f"audio_files/{audio_file_name}"

        log_file_path = f"logs/log_{datetime.now().strftime('%Y%m%d')}.txt"

        self.progress_dialog = QProgressDialog("변환 중...", None, 0, 0, self)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.show()

        self.worker = Worker(audio_file_path, log_file_path)
        self.worker.progress.connect(self.show_progress)
        self.worker.start()

    def show_progress(self, message):
        self.progress_dialog.cancel()
        QMessageBox.information(self, "Information", message)
        self.update_text_file_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioToTextApp()
    window.show()
    sys.exit(app.exec_())
