import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
from io import BytesIO

class ImageRenamer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('이미지 파일 이름 변경기')
        self.setGeometry(100, 100, 1000, 600)  # 윈도우 위치와 크기 설정
        self.setFixedSize(1000, 600)  # 창 크기를 고정

        # 메인 수평 레이아웃
        self.mainLayout = QHBoxLayout()

        # 파일 목록을 위한 왼쪽 레이아웃
        self.leftLayout = QVBoxLayout()

        self.directoryButton = QPushButton('디렉토리 선택', self)
        self.directoryButton.clicked.connect(self.selectDirectory)
        self.leftLayout.addWidget(self.directoryButton)

        self.listWidget = QListWidget(self)
        self.listWidget.clicked.connect(self.onFileSelect)
        self.listWidget.currentRowChanged.connect(self.onFileSelect)
        self.leftLayout.addWidget(self.listWidget)

        # 이미지를 표시할 오른쪽 레이아웃
        self.rightLayout = QVBoxLayout()

        self.imageLabel = QLabel(self)
        self.imageLabel.setFixedSize(400, 400)  # 이미지 표시 영역의 크기를 고정
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.rightLayout.addWidget(self.imageLabel)

        # 파일명을 입력하고 버튼을 추가할 하단 레이아웃
        self.bottomLayout = QVBoxLayout()
        
        self.newNameLabel = QLabel('새 파일명:', self)
        self.bottomLayout.addWidget(self.newNameLabel)

        self.newNameEdit = QLineEdit(self)
        self.newNameEdit.returnPressed.connect(self.renameFile)  # 엔터 키로 파일 이름 변경
        self.bottomLayout.addWidget(self.newNameEdit)

        self.renameButton = QPushButton('파일 이름 변경', self)
        self.renameButton.clicked.connect(self.renameFile)
        self.bottomLayout.addWidget(self.renameButton)

        self.rightLayout.addLayout(self.bottomLayout)

        # 왼쪽과 오른쪽 레이아웃을 메인 레이아웃에 추가
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)

        self.setLayout(self.mainLayout)
        self.imageCache = {}

    def selectDirectory(self):
        self.directory = str(QFileDialog.getExistingDirectory(self, "디렉토리 선택"))
        if self.directory:
            self.loadFiles()

    def loadFiles(self):
        self.listWidget.clear()
        self.imageCache.clear()
        self.files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        self.listWidget.addItems(self.files)
        if self.files:
            self.listWidget.setCurrentRow(0)  # 첫 번째 파일을 자동으로 선택

    def onFileSelect(self):
        selected_file = self.listWidget.currentItem()
        if selected_file:
            self.displayImage(selected_file.text())

    def displayImage(self, file_name):
        file_path = os.path.join(self.directory, file_name)
        if file_path not in self.imageCache:
            image = Image.open(file_path)
            image.thumbnail((400, 400))
            buffer = BytesIO()
            image.save(buffer, format="PNG")
            buffer.seek(0)
            pixmap = QPixmap()
            pixmap.loadFromData(buffer.read())
            self.imageCache[file_path] = pixmap
        else:
            pixmap = self.imageCache[file_path]

        self.imageLabel.setPixmap(pixmap)

    def renameFile(self):
        if not hasattr(self, 'directory') or not self.directory:
            QMessageBox.critical(self, "오류", "디렉토리를 선택하세요.")
            return

        selected_file = self.listWidget.currentItem()
        if not selected_file:
            QMessageBox.critical(self, "오류", "파일을 선택하세요.")
            return

        new_name = self.newNameEdit.text().strip()
        if not new_name:
            QMessageBox.critical(self, "오류", "새 파일명을 입력하세요.")
            return

        old_file = selected_file.text()
        old_file_path = os.path.join(self.directory, old_file)
        file_name, file_extension = os.path.splitext(old_file)
        new_file_path = os.path.join(self.directory, f"{new_name}{file_extension}")

        if os.path.exists(new_file_path):
            QMessageBox.critical(self, "오류", "같은 이름의 파일이 이미 존재합니다. 다른 이름을 입력하세요.")
            return

        os.rename(old_file_path, new_file_path)
        self.loadFiles()  # 파일 목록을 갱신
        self.newNameEdit.clear()
        self.imageLabel.clear()  # 이미지 라벨 초기화
        QMessageBox.information(self, "성공", "파일 이름이 성공적으로 변경되었습니다.")
        # 변경된 파일 선택 및 이미지 갱신
        for i in range(self.listWidget.count()):
            if self.listWidget.item(i).text() == new_name + file_extension:
                self.listWidget.setCurrentRow(i)
                self.onFileSelect()
                break

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            current_row = self.listWidget.currentRow()
            if current_row > 0:
                self.listWidget.setCurrentRow(current_row - 1)
                self.onFileSelect()
        elif event.key() == Qt.Key_Down:
            current_row = self.listWidget.currentRow()
            if current_row < self.listWidget.count() - 1:
                self.listWidget.setCurrentRow(current_row + 1)
                self.onFileSelect()
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.newNameEdit.hasFocus():
                self.renameFile()
            else:
                self.newNameEdit.setFocus()
                self.onFileSelect()
        else:
            super().keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageRenamer()
    ex.show()
    sys.exit(app.exec_())
