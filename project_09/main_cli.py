import speech_recognition as sr
from gtts import gTTS

def record_audio():
    # 음성 인식 객체 생성
    recognizer = sr.Recognizer()

    # 마이크로부터 음성 입력 받기
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    # 음성을 텍스트로 변환
    try:
        text = recognizer.recognize_google(audio, language='ko-KR')
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def text_to_speech(text, output_filename="output_audio.mp3"):
    # 텍스트를 음성으로 변환
    tts = gTTS(text=text, lang='ko')
    # 음성 파일 저장
    tts.save(output_filename)
    print(f"Saved audio to {output_filename}")

if __name__ == "__main__":
    # 마이크로부터 음성 입력 받아 텍스트로 변환
    text = record_audio()
    if text:
        # 변환된 텍스트를 음성 파일로 저장
        text_to_speech(text)
