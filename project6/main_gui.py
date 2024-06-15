import sys
import os
import shutil
import io
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QListWidget, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QProgressDialog
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import speech_recognition as sr
from pydub import AudioSegment

# 변환 작업을 별도의 스레드에서 실행하기 위한 Worker 클래스
class Worker(QThread):
    progress = pyqtSignal(str)  # 진행 상황을 전달하는 시그널

    def __init__(self, audio_file_path, log_file_path):
        super().__init__()
        self.audio_file_path = audio_file_path
        self.log_file_path = log_file_path

    def run(self):
        recognizer = sr.Recognizer()
        file_extension = os.path.splitext(self.audio_file_path)[1].lower()
        file_name = os.path.splitext(os.path.basename(self.audio_file_path))[0]
        text_file_path = f"text_files/{file_name}.txt"

        # 로그 파일에 기록
        with open(self.log_file_path, 'a', encoding='utf-8') as log_file:
            if os.path.exists(text_file_path):
                log_file.write(f"{datetime.now()} - {self.audio_file_path} - 이미 존재함\n")
                self.progress.emit(f"{text_file_path} 이미 존재합니다. 변환을 건너뜁니다.")
                return

            # MP3 파일을 WAV 파일로 변환
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
                    # 구글 음성 인식 API를 사용하여 음성을 텍스트로 변환
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

# 메인 애플리케이션 클래스
class AudioToTextApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Audio to Text Converter")
        self.setGeometry(100, 100, 800, 400)

        self.create_folders()
        self.move_audio_files_to_folder()

        self.layout = QHBoxLayout()

        # 오디오 파일 목록 레이아웃
        self.audio_files_layout = QVBoxLayout()
        self.audio_files_label = QLabel("audio_files 폴더 내의 파일 목록:")
        self.audio_files_layout.addWidget(self.audio_files_label)

        self.audio_file_list = QListWidget()
        self.update_audio_file_list()
        self.audio_files_layout.addWidget(self.audio_file_list)

        # 변환 버튼
        self.convert_button = QPushButton("변환")
        self.convert_button.clicked.connect(self.convert_selected_file)
        self.audio_files_layout.addWidget(self.convert_button)

        # 오디오 파일 삭제 버튼
        self.delete_audio_button = QPushButton("오디오 파일 삭제")
        self.delete_audio_button.clicked.connect(self.delete_selected_audio_file)
        self.audio_files_layout.addWidget(self.delete_audio_button)

        self.layout.addLayout(self.audio_files_layout)

        # 텍스트 파일 목록 레이아웃
        self.text_files_layout = QVBoxLayout()
        self.text_files_label = QLabel("변환된 텍스트 파일 목록:")
        self.text_files_layout.addWidget(self.text_files_label)

        self.text_file_list = QListWidget()
        self.update_text_file_list()
        self.text_files_layout.addWidget(self.text_file_list)

        # 텍스트 파일 삭제 버튼
        self.delete_text_button = QPushButton("텍스트 파일 삭제")
        self.delete_text_button.clicked.connect(self.delete_selected_text_file)
        self.text_files_layout.addWidget(self.delete_text_button)

        self.layout.addLayout(self.text_files_layout)

        # 종료 버튼
        self.exit_button = QPushButton("종료")
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    # 필요한 폴더 생성
    def create_folders(self):
        if not os.path.exists('audio_files'):
            os.makedirs('audio_files')
        if not os.path.exists('text_files'):
            os.makedirs('text_files')
        if not os.path.exists('logs'):
            os.makedirs('logs')

    # 오디오 파일을 audio_files 폴더로 이동
    def move_audio_files_to_folder(self):
        audio_extensions = ['.mp3', '.wav']
        for file in os.listdir('.'):
            if os.path.isfile(file) and os.path.splitext(file)[1].lower() in audio_extensions:
                shutil.move(file, f"audio_files/{file}")

    # 오디오 파일 목록 업데이트
    def update_audio_file_list(self):
        self.audio_file_list.clear()
        files = os.listdir('audio_files')
        for file in files:
            self.audio_file_list.addItem(file)

    # 텍스트 파일 목록 업데이트
    def update_text_file_list(self):
        self.text_file_list.clear()
        files = os.listdir('text_files')
        for file in files:
            self.text_file_list.addItem(file)

    # 선택된 오디오 파일을 변환
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

    # 진행 상황을 보여주는 메서드
    def show_progress(self, message):
        self.progress_dialog.cancel()
        QMessageBox.information(self, "Information", message)
        self.update_text_file_list()

    # 선택된 오디오 파일 삭제
    def delete_selected_audio_file(self):
        selected_items = self.audio_file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "파일을 선택하세요")
            return

        audio_file_name = selected_items[0].text()
        audio_file_path = f"audio_files/{audio_file_name}"

        reply = QMessageBox.question(self, "확인", f"{audio_file_name}을(를) 삭제하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.remove(audio_file_path)
            self.update_audio_file_list()

    # 선택된 텍스트 파일 삭제
    def delete_selected_text_file(self):
        selected_items = self.text_file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "파일을 선택하세요")
            return

        text_file_name = selected_items[0].text()
        text_file_path = f"text_files/{text_file_name}"

        reply = QMessageBox.question(self, "확인", f"{text_file_name}을(를) 삭제하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.remove(text_file_path)
            self.update_text_file_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioToTextApp()
    window.show()
    sys.exit(app.exec_())
