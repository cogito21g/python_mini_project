import speech_recognition as sr
from gtts import gTTS

def choose_language():
    print("Choose the language for speech recognition:")
    print("1: English")
    print("2: Korean")
    print("3: Chinese")
    print("4: Japanese")
    print("5: Spanish")
    print("6: German")
    print("7: French")
    choice = input("Enter the number of your choice: ")
    
    language_mapping = {
        '1': 'en-US',
        '2': 'ko-KR',
        '3': 'zh-CN',
        '4': 'ja-JP',
        '5': 'es-ES',
        '6': 'de-DE',
        '7': 'fr-FR'
    }
    
    return language_mapping.get(choice, 'en-US')

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

def text_to_speech(text, language, output_audio_filename="output_audio.mp3"):
    # 텍스트를 음성으로 변환
    tts = gTTS(text=text, lang=language)
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
    language_code = choose_language()
    # 마이크로부터 음성 입력 받아 텍스트로 변환
    text = record_audio(language_code)
    if text:
        # 변환된 텍스트를 음성 파일로 저장
        text_to_speech(text, language_code.split('-')[0])
        # 변환된 텍스트를 텍스트 파일로 저장
        save_text_to_file(text)
