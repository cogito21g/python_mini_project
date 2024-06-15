import os
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

def convert_audio_to_text(audio_file_path):
    """
    Convert audio file to text using Google Web Speech API and save the transcription to a text file.

    Parameters:
    audio_file_path (str): Path to the input audio file.
    """
    # Get the file name without extension
    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    output_text_file = f"{base_name}.txt"

    # Check if the transcription file already exists
    if os.path.exists(output_text_file):
        print(f"{output_text_file} already exists. Skipping transcription.")
        return

    try:
        # Convert audio file to WAV format in memory
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
        
        # Export audio to a BytesIO object in WAV format
        wav_io = BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Load the WAV data from BytesIO object
        with sr.AudioFile(wav_io) as source:
            audio_data = recognizer.record(source)  # Record the audio file using recognizer

        # Convert the audio to text
        try:
            text = recognizer.recognize_google(audio_data, language="en-US")  # Use 'en-US' for English
            with open(output_text_file, 'w') as f:
                f.write(text)
            print(f"Transcription saved to {output_text_file}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    except ValueError as ve:
        print(ve)

# Example usage
audio_file_path = input("Enter the path to the audio file: ")  # Get the audio file path from user input
convert_audio_to_text(audio_file_path)
