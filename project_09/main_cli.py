import speech_recognition as sr
from gtts import gTTS

def choose_language():
    print("Choose the language for speech recognition:")
    print("1: English")
    print("2: Korean")
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        return 'en-US'
    elif choice == '2':
        return 'ko-KR'
    else:
        print("Invalid choice. Defaulting to English.")
        return 'en-US'

def record_audio(language):
    # 음성 인식 객체 생성
    recognizer = sr.Recognizer()

    # 마이크로부터 음성 입력 받기
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    # 음성을 텍스트로 변환
    try:
        text = recognizer.recognize_google(audio, language=language)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def text_to_speech(text, output_audio_filename="output_audio.mp3"):
    # 텍스트를 음성으로 변환
    tts = gTTS(text=text, lang='en')
    # 음성 파일 저장
    tts.save(output_audio_filename)
    print(f"Saved audio to {output_audio_filename}")

def save_text_to_file(text, output_text_filename="output_text.txt"):
    # 텍스트 파일 저장
    with open(output_text_filename, "w", encoding="utf-8") as text_file:
        text_file.write(text)
    print(f"Saved text to {output_text_filename}")

if __name__ == "__main__":
    # 언어 선택
    language = choose_language()
    # 마이크로부터 음성 입력 받아 텍스트로 변환
    text = record_audio(language)
    if text:
        # 변환된 텍스트를 음성 파일로 저장
        text_to_speech(text)
        # 변환된 텍스트를 텍스트 파일로 저장
        save_text_to_file(text)
