# Python Mini Project

## Introduction
- 파이썬을 활용한 간단한 자동화 프로젝트를 기록하는 공간입니다. 

## Projects
1. [여러개의 파일 자동 생성](#project_01-여러개의-파일-자동-생성)
2. [파일 선택해서 이름 변경하기](#project_02-파일-선택해서-이름-변경하기)
3. [이미지 파일 확인하고 이름 변경](#project_03-이미지-파일-확인하고-이름-변경하기)
4. [텍스트를 음성으로 변환하여 저장하기](#project_04-텍스트를-음성으로-변환하여-저장하기)
5. [텍스트 파일을 음성 파일로 변경하기](#project_05-텍스트-파일을-음성-파일로-변경하기)
6. [텍스트 파일들을 음성 파일들로 변환하기](#project_06-텍스트-파일들을-음성-파일들로-변환하기)
7. [음성파일을 텍스트로 변환하기](#project_07-음성파일을-텍스트로-변환하기)
8. [음성 파일들을 텍스트 파일들로 변환하기](#project_08-음성-파일들을-텍스트-파일들로-변환하기)
9. [](#project_09-이미지-파일-이름-변경-및-정보-저장하기)
10.[](#project_10-음성-파일-이름-변경-및-정보-저장하기)

### Project_01: [여러개의 파일 자동 생성](./project_01/)

- 폴더명, 파일명, 개수와 확장자를 입력 받아 자동으로 파일을 생성

``` python
# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

### Project_02: [파일 선택해서 이름 변경하기](./project_02/)

- 파일명 변경하기

``` python
# CLI 환경
python main_cli.py

# GUI 환경
python main_gui.py
```

### Project_03: [이미지 파일 확인하고 이름 변경하기](./project_03/)

- 이미지 파일 확인하면서 이름 변경하기
- 엔터로 변경 확인 가능 
- 탭으로 파일 리스트, 변경 입력창 번갈아 이동

``` python
# CLI 환경
python main_tkinter.py

# GUI 환경
python main_qt.py
```

### Project_04: [텍스트를 음성으로 변환하여 저장하기](./project_04/)

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



### Project_05: [텍스트 파일을 음성 파일로 변경하기](./project_05/)

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


### Project_06: [텍스트 파일들을 음성 파일들로 변환하기](./project_06/)

1. 텍스트 파일 선택
- 사용자는 `text_files` 폴더 내의 파일 목록을 보고, 변환할 파일의 번호를 입력하여 여러 파일을 선택할 수 있습니다.
- 선택된 파일 번호는 쉼표로 구분하여 입력합니다.

2. 출력 파일 이름 지정
- 각 텍스트 파일에 대해 변환된 음성 파일의 이름을 지정할 수 있습니다.
- 기본 파일 이름은 "output"이며, 사용자가 직접 이름을 입력하지 않으면 "output.mp3"로 저장됩니다.

3. 텍스트를 음성 파일로 변환
- 선택한 각 텍스트 파일을 읽어 Google Text-to-Speech (`gTTS`)를 사용하여 음성 파일로 변환합니다.
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
```python
# 라이브러리 설치
pip install gtts 

# cli 실행
python main_cli.py

# 텍스트와 동일한 이름의 음성 파일 생성
python main_cli2.py 

# gui 실행
python main_gui.py
```

##### 라이브러리
- - gTTS (Google Text-to-Speech): Google의 텍스트-음성 변환 API를 사용하는 Python 라이브러리. 입력된 텍스트를 다양한 언어로 음성 파일로 변환


### Project_07: [음성파일을 텍스트로 변환하기](./project_07/)

1. 변환 언어 선택
2. 파일 목록 표시
3. 텍스트 파일 생성
- 선택된 음성 파일과 동일한 이름의 텍스트 파일을 text_files에 생성

##### Usage
```python
# 라이브러리 설치
pip install SpeechRecognition pydub tqdm PyQt5

# cli 실행
python main_cli.py

# cli 실행
python main_cli.py
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


### Project_08: [음성 파일들을 텍스트 파일들로 변환하기](./project_08/)

1. 변환 언어 선택
2. 파일 목록 표시
3. 파일들 선택
- 파일 목록에 표시된 파일들의 번호틑 ,(콤마)를 사용하여 나열
- 순차적으로 변환후 log에 기록

##### Usage
```python
# 라이브러리 설치
pip install SpeechRecognition pydub PyQt5

# cli 실행
python main_cli.py
```

##### 라이브러리
- speech_recognition: Google Speech Recognition API 사용
- pydub: 오디오 처리 라이브러리
    - 오디오 파일을 변환, 자르기, 결합, 페이드 인/아웃, 볼륨 조절 등의 작업 수행
    - 다양한 오디오 파일 형식(MP3, WAV, FLAC 등)을 지원
    - pydub는 FFmpeg나 libav와 같은 외부 프로그램을 필요
- PyQt5: Python에서 Qt 프레임워크를 사용


### Project_09: [음성을 입력 받아 음성 파일과 텍스트 생성](./project_09/)

1. 언어 선택
- 사용자가 음성 인식에 사용할 언어를 선택
- 지원되는 언어: English (en-US) / Korean (ko-KR) / Chinese (zh-CN) / Japanese (ja-JP) / Spanish (es-ES) / German (de-DE) / French (fr-FR)

2. 파일명 입력
- 사용자는 저장할 파일의 기본 이름을 입력
- 입력된 이름은 음성 파일(`.mp3`)과 텍스트 파일(`.txt`)에 공통으로 사용
- 파일 이름이 이미 존재하는 경우, 중복을 피하기 위해 다른 이름을 입력하도록 요청

3. 음성 입력
- 마이크를 통해 사용자의 음성을 입력
- 입력된 음성을 Google Speech Recognition을 통해 텍스트로 변환

4. 파일 저장
- 변환된 텍스트를 음성 파일(`.mp3`)로 저장
- 동일한 텍스트를 텍스트 파일(`.txt`)로 저장
- 파일은 언어별로 `audio_files` 및 `text_files` 디렉토리에 저장
    - 예: 한국어 파일은 `audio_files/ko` 및 `text_files/ko` 폴더에 저장

5. 반복 입력
- 사용자는 여러 번 파일을 입력하고 저장할 수 있습니다.
- `exit`를 입력하면 프로그램이 종료됩니다.


##### 실행 방법
```python
# 라이브러리 설치
pip install SpeechRecognition pydub gtts
pip install pyaudio

# cli 실행
python main_cli.py
```

#### 사용 방법

1. 프로그램을 실행합니다.
2. 언어 선택 메뉴에서 원하는 언어의 번호를 입력합니다.
3. 파일 이름을 입력합니다. (확장자는 입력하지 마세요)
4. 동일한 이름의 파일이 이미 존재하면, 다른 파일 이름을 입력합니다.
5. 마이크가 켜지면 음성을 입력합니다.
6. 음성 인식이 완료되면, 변환된 텍스트가 음성 파일과 텍스트 파일로 저장됩니다.
7. 파일 이름을 계속 입력하여 반복적으로 음성을 녹음하고 저장할 수 있습니다.
8. `exit`를 입력하면 프로그램이 종료됩니다.



### Project_10: 음성 파일 이름 변경 및 정보 저장하기

1. 디렉토리 생성 및 확인
- audio_files와 text_files 디렉토리가 존재하지 않을 경우 자동으로 생성

2. 음성 파일 목록 출력
- audio_files 디렉토리 내의 .mp3 파일 목록을 번호와 함께 출력

3. 파일 재생 및 중지
- 사용자가 번호나 파일 이름을 입력하면 해당 파일을 pygame을 사용해 재생
- 's'를 입력하면 현재 재생 중인 음악을 중지

4. 파일명 변경
- 사용자가 선택한 파일의 새 이름을 입력받고, 해당 이름으로 파일명을 변경
- 새 파일명이 중복되지 않도록 확인

5. 텍스트 파일 생성 및 기록
- 사용자가 입력한 정보를 text_files 디렉토리에 음악 파일명과 동일한 이름의 텍스트 파일에 저장
- 텍스트 파일이 이미 존재할 경우 경고 메시지를 출력하고 덮어쓰지 않도록 함

##### Usage
```python
# 라이브러리 설치
pip install 

# cli 실행
python main_cli.py
```

##### 라이브러리
- 


### Project_11: 이미지 파일 이름 변경 및 정보 저장하기

1. 이미지 파일 확인
2. 파일명, 정보 입력
- 파일명은 변경
- 정보는 해당 파일명의 텍스트로 변경

##### Usage
```python
# 라이브러리 설치
pip install 

# cli 실행
python main_cli.py

# gui 실행
python main_gui.py
```

##### 라이브러리
- 

### Project_12: 동영상 파일 이름 변경 및 정보 저장하기

1. 동영상 파일 확인
2. 파일명, 정보 입력
- 파일명은 변경
- 정보는 해당 파일명의 텍스트로 변경

##### Usage
```python
# 라이브러리 설치
pip install 

# cli 실행
python main_cli.py

# gui 실행
python main_gui.py
```

##### 라이브러리
- 

