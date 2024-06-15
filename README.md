# Python Mini Project

## Introduction
- 파이썬을 활용한 간단한 자동화 프로젝트를 기록하는 공간입니다. 

## Projects
- [여러개의 파일 자동 생성](./project1/)
- [파일 이름 변경](./project2/)
- [이미지 파일 확인하고 이름 변경](./project3/)
- [텍스트를 음성으로 변환하기](./project4/)
- []()
- []()

### Project1: 여러개의 파일 자동 생성

- 폴더명, 파일명, 개수와 확장자를 입력 받아 자동으로 파일을 생성

``` python
# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

### Project2: 파일 선택해서 이름 변경하기

- 파일명 변경하기

``` python
# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

### Project3: 이미지 파일 확인하고 이름 변경하기

- 이미지 파일 확인하면서 이름 변경하기
- 엔터로 변경 확인 가능 
- 탭으로 파일 리스트, 변경 입력창 번갈아 이동

``` python
# CLI 환경
python main_tkinter.py

# GUI 환경
python main_qt.py
```

#### Project4: 텍스트를 음성으로 변환하여 저장하기

- 텍스트를 직접 입력하거나 텍스트 파일을 불러와서 음성으로 변환하여 저장


``` python
# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

#### Project5: 여러 텍스트 파일들을 음성 파일로 변경하기




#### Project_06: [음성파일을 텍스트로 변환하기](./project_06/)

1. 폴더 생성 및 파일 이동

- audio_files, text_files, logs 폴더가 존재하지 않으면 생성합니다.
- 현재 디렉터리에서 MP3 및 WAV 파일을 audio_files 폴더로 이동합니다.

2. GUI 구성 요소

- 오디오 파일 목록: audio_files 폴더 내의 오디오 파일 목록을 표시합니다.
- 텍스트 파일 목록: text_files 폴더 내의 텍스트 파일 목록을 표시합니다.
- 변환 버튼: 선택된 오디오 파일을 텍스트 파일로 변환합니다.
- 삭제 버튼: 선택된 오디오 파일 또는 텍스트 파일을 삭제합니다.
- 종료 버튼: 애플리케이션을 종료합니다.

3. 오디오 파일 변환 기능

- 선택된 오디오 파일을 구글 음성 인식 API를 사용하여 텍스트 파일로 변환합니다.
- 변환 중에는 QProgressDialog를 사용하여 로딩 창을 표시합니다.
- 변환이 완료되면 변환된 텍스트 파일 목록을 업데이트하고, 결과를 사용자에게 알립니다.
- 변환 로그를 날짜별로 기록합니다.

4. 파일 삭제 기능

- 선택된 오디오 파일 또는 텍스트 파일을 삭제합니다.
- 파일을 삭제하기 전에 확인 메시지를 표시하여 실수를 방지합니다.

##### Usage
```python
# 라이브러리 설치
pip install SpeechRecognition pydub tqdm PyQt5 pyinstaller

# cli 실행
python main_cli.py

# gui 실행
python main_gui.py

# 실행 파일 생성
pyinstaller --onefile --windowed main_gui.py
```

##### 라이브러리
- speech_recognition: Google Speech Recognition API 사용
- pydub: 오디오 처리 라이브러리
    - 오디오 파일을 변환, 자르기, 결합, 페이드 인/아웃, 볼륨 조절 등의 작업 수행
    - 다양한 오디오 파일 형식(MP3, WAV, FLAC 등)을 지원
    - pydub는 FFmpeg나 libav와 같은 외부 프로그램을 필요
- tqdm: 프로그레스 바(progress bar)를 제공
- io.BytesIO: 메모리내 파일 처리
- PyQt5: Python에서 Qt 프레임워크를 사용


#### Project_

- 

```python

```


#### Projects6: 음성파일과 이미지 파일을 결합하여 동영상 파일 만들기
```python

```




#### Project7: 코딩테스트 문제 기록하는 Markdown 파일 만들기

- 사이트 선택
- 언어 선택
- 문제 링크 기록 및 문제 유형
- 해설 코드 및 코드 설졍
- 테스트 코드

#### Project8: 영어 단어장으로 퀴즈 생성하기

- 영어 퀴즈 게임 만들기


#### Project9: 숏폼 비디오 만들기

- 음성파일과 이미지 합치기
- 이미지에 변환을 주어 움직이는 효과 주기
- 입력한 스크립트에 맞추어 음성 파일을 만들고 이후 음성파일과 이미지 파일을 순서대로 합치기

#### Project10: 비디오 편집기 만들기

#### Project11: 파일 확장자 변경하기

- 이미지 파일
- 음성 파일
- 텍스트 파일