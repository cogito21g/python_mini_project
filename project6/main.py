# 필요한 라이브러리를 불러옵니다.
import speech_recognition as sr
from pydub import AudioSegment
import os

# 음성 파일을 텍스트로 변환하는 함수입니다.
def convert_audio_to_text(audio_file_path):
    # Recognizer 객체를 생성합니다.
    recognizer = sr.Recognizer()
    
    # 파일 확장자를 확인합니다.
    file_extension = os.path.splitext(audio_file_path)[1].lower()
    
    # 파일 확장자에 따라 변환을 처리합니다.
    if file_extension == '.mp3':
        # MP3 파일을 WAV 파일로 변환합니다.
        audio = AudioSegment.from_mp3(audio_file_path)
        wav_path = audio_file_path.replace('.mp3', '.wav')
        audio.export(wav_path, format='wav')
        audio_file_path = wav_path
    elif file_extension != '.wav':
        return "지원되지 않는 파일 형식입니다."

    # 음성 파일을 불러옵니다.
    with sr.AudioFile(audio_file_path) as source:
        # 오디오 데이터를 읽습니다.
        audio_data = recognizer.record(source)

        try:
            # 구글 음성 인식 API를 사용하여 음성을 텍스트로 변환합니다.
            text = recognizer.recognize_google(audio_data, language='ko-KR')
            return text
        except sr.UnknownValueError:
            # 음성을 인식할 수 없는 경우
            return "음성을 인식할 수 없습니다."
        except sr.RequestError as e:
            # API 요청 에러가 발생한 경우
            return f"API 요청 에러: {e}"

# 변환할 음성 파일 경로를 지정합니다.
audio_file_path = "test.mp3"  # 확장자를 포함한 파일 경로

# 음성 파일을 텍스트로 변환합니다.
text = convert_audio_to_text(audio_file_path)

# 변환된 텍스트를 출력합니다.
print(text)
