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

### Project_01: 여러개의 파일 자동 생성

- 폴더명, 파일명, 개수와 확장자를 입력 받아 자동으로 파일을 생성

``` python
# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

### Project_02: 파일 선택해서 이름 변경하기

- 파일명 변경하기

``` python
# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

### Project_03: 이미지 파일 확인하고 이름 변경하기

- 이미지 파일 확인하면서 이름 변경하기
- 엔터로 변경 확인 가능 
- 탭으로 파일 리스트, 변경 입력창 번갈아 이동

``` python
# CLI 환경
python main_tkinter.py

# GUI 환경
python main_qt.py
```

#### Project_04: [텍스트를 음성으로 변환하여 저장하기](./project_04/)

1. 텍스트 입력
- 사용자는 변환할 텍스트를 텍스트 박스에 입력합니다.

2. 파일 이름 입력
- 사용자는 저장할 파일 이름을 입력합니다. (확장자 없이)

3. 언어 코드 입력
- 사용자는 텍스트의 언어 코드를 입력할 수 있습니다. 기본값은 영어('en')입니다.

4. 파일 저장
- "변환 및 저장" 버튼을 클릭하면 입력된 텍스트가 지정된 언어로 음성 파일(.mp3)과 텍스트 파일(.txt)로 변환되어 저장됩니다.
- 오디오 파일은 audio_files 폴더에, 텍스트 파일은 text_files 폴더에 저장됩니다.

5. 중복 파일 확인
- 저장할 파일 이름이 이미 존재하는 경우, 오류 메시지가 표시되고 다른 파일 이름을 입력하도록 요청합니다.

6. 예외 처리 및 재시작:
- 프로그램 실행 중 예외가 발생할 경우, 오류 메시지를 표시하고 프로그램을 재시작합니다.

##### Usage

``` python
# 라이브러리 설치
pip install gtts

# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

##### 라이브러리
- gTTS (Google Text-to-Speech): Google의 텍스트-음성 변환 API를 사용하는 Python 라이브러리. 입력된 텍스트를 다양한 언어로 음성 파일로 변환



#### Project_05: [텍스트 파일을 음성 파일로 변경하기](./project_05/)

1. 텍스트 파일 선택
- 사용자는 `text_files` 폴더에서 텍스트 파일을 선택할 수 있습니다.
- 파일 선택 다이얼로그를 통해 파일을 선택하면 선택된 파일의 경로가 표시됩니다.

2. 출력 파일 이름 지정
- 사용자는 변환된 음성 파일의 이름을 지정할 수 있습니다.
- 기본 파일 이름은 "output"이며, 사용자가 직접 이름을 입력하지 않으면 "output.mp3"로 저장됩니다.

3. 텍스트 파일을 음성 파일로 변환
- 선택한 텍스트 파일을 읽어 Google Text-to-Speech (`gTTS`)를 사용하여 음성 파일로 변환합니다.
- 변환된 음성 파일은 `audio_files` 폴더에 저장됩니다.

4. 로그 기록
- 변환 작업이 완료되면 날짜와 시간을 포함한 로그 메시지를 기록합니다.
- 로그 파일은 `log` 폴더에 날짜별로 저장되며, 기존 파일이 있을 경우 내용을 추가합니다.

5. 폴더 및 파일 관리
- 애플리케이션 실행 시 `text_files` 및 `audio_files` 폴더가 존재하지 않으면 생성합니다.
- 현재 디렉토리의 모든 텍스트 파일을 `text_files` 폴더로 이동합니다.

6. 에러 처리
- 변환할 텍스트 파일이 선택되지 않은 경우 경고 메시지를 표시합니다.
- 지정된 출력 파일명이 이미 존재하는 경우 경고 메시지를 표시하고 다른 이름을 선택하도록 합니다.
- 변환 과정 중 오류가 발생하면 오류 메시지를 표시합니다.

##### Usage

``` python
# 라이브러리 설치
pip install gtts 

# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

##### 라이브러리
- gTTS (Google Text-to-Speech): Google의 텍스트-음성 변환 API를 사용하는 Python 라이브러리. 입력된 텍스트를 다양한 언어로 음성 파일로 변환


#### Project_07: [음성파일을 텍스트로 변환하기](./project_06/)

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