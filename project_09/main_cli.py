import speech_recognition as sr
from gtts import gTTS
import os

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
        '1': ('en-US', 'en'),
        '2': ('ko-KR', 'ko'),
        '3': ('zh-CN', 'zh'),
        '4': ('ja-JP', 'ja'),
        '5': ('es-ES', 'es'),
        '6': ('de-DE', 'de'),
        '7': ('fr-FR', 'fr')
    }
    
    return language_mapping.get(choice, ('en-US', 'en'))

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

def text_to_speech(text, language, output_audio_filename):
    # 텍스트를 음성으로 변환
    tts = gTTS(text=text, lang=language)
    # 음성 파일 저장
    tts.save(output_audio_filename)
    print(f"Saved audio to {output_audio_filename}")

def save_text_to_file(text, output_text_filename):
    # 텍스트 파일 저장
    with open(output_text_filename, "w", encoding="utf-8") as text_file:
        text_file.write(text)
    print(f"Saved text to {output_text_filename}")

def create_directories(language_code):
    audio_dir = os.path.join('audio_files', language_code)
    text_dir = os.path.join('text_files', language_code)
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(text_dir, exist_ok=True)
    return audio_dir, text_dir

if __name__ == "__main__":
    # 언어 선택
    language_code, tts_language = choose_language()
    # 디렉토리 생성
    audio_dir, text_dir = create_directories(language_code.split('-')[0])
    
    while True:
        # 파일명 입력
        file_name = input("Enter the base name for the files (without extension, type 'exit' to quit): ")
        if file_name.lower() == 'exit':
            break
        
        audio_filename = os.path.join(audio_dir, f"{file_name}.mp3")
        text_filename = os.path.join(text_dir, f"{file_name}.txt")
        
        if os.path.exists(audio_filename) or os.path.exists(text_filename):
            print("A file with that name already exists. Please choose a different name.")
            continue
        
        # 마이크로부터 음성 입력 받아 텍스트로 변환
        text = record_audio(language_code)
        if text:
            # 변환된 텍스트를 음성 파일로 저장
            text_to_speech(text, tts_language, audio_filename)
            # 변환된 텍스트를 텍스트 파일로 저장
            save_text_to_file(text, text_filename)
