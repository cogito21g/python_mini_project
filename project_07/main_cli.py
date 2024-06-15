import os
import speech_recognition as sr
from pydub import AudioSegment

def convert_audio_to_wav(audio_file_path):
    file_extension = os.path.splitext(audio_file_path)[1].lower()
    audio = None
    
    if file_extension == '.mp3':
        audio = AudioSegment.from_mp3(audio_file_path)
    elif file_extension == '.wav':
        audio = AudioSegment.from_wav(audio_file_path)
    elif file_extension == '.ogg':
        audio = AudioSegment.from_ogg(audio_file_path)
    elif file_extension == '.flv':
        audio = AudioSegment.from_flv(audio_file_path)
    elif file_extension == '.mp4':
        audio = AudioSegment.from_file(audio_file_path, "mp4")
    elif file_extension == '.wma':
        audio = AudioSegment.from_file(audio_file_path, "wma")
    else:
        raise ValueError("Unsupported file format")
    
    wav_file_path = "converted_audio.wav"
    audio.export(wav_file_path, format="wav")
    return wav_file_path

def convert_audio_to_text(audio_file_path):
    try:
        wav_file_path = convert_audio_to_wav(audio_file_path)
        
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Load the WAV file
        with sr.AudioFile(wav_file_path) as source:
            audio_data = recognizer.record(source)  # Use recognizer to record the audio file

        # Convert the audio to text
        try:
            text = recognizer.recognize_google(audio_data, language="ko-KR")
            print("Transcription: ", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    except ValueError as ve:
        print(ve)

# Example usage
audio_file_path = "test.mp3"  # Replace with your audio file path
convert_audio_to_text(audio_file_path)
