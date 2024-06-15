import os
import shutil
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

# Ensure the audio_files and text_files directories exist
os.makedirs('audio_files', exist_ok=True)
os.makedirs('text_files', exist_ok=True)

def move_files_to_audio_folder():
    """
    Move all audio files from the current directory to the audio_files directory.
    """
    supported_formats = ('.mp3', '.wav', '.ogg', '.flv', '.mp4', '.wma')
    for file_name in os.listdir('.'):
        if file_name.lower().endswith(supported_formats):
            shutil.move(file_name, os.path.join('audio_files', file_name))

def convert_audio_to_text(audio_file_path):
    """
    Convert audio file to text using Google Web Speech API and save the transcription to a text file.

    Parameters:
    audio_file_path (str): Path to the input audio file.
    """
    # Get the file name without extension
    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    output_text_file = os.path.join('text_files', f"{base_name}.txt")

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

# Move all supported audio files to the audio_files directory
move_files_to_audio_folder()

# List all audio files in the audio_files directory
audio_files = os.listdir('audio_files')
if not audio_files:
    print("No audio files found in the audio_files directory.")
else:
    print("Available audio files:")
    for idx, file_name in enumerate(audio_files, start=1):
        print(f"{idx}. {file_name}")

    # Get the user's choice of audio file
    choice = int(input("Enter the number of the audio file to transcribe: "))
    chosen_file = audio_files[choice - 1]
    chosen_file_path = os.path.join('audio_files', chosen_file)

    # Convert the chosen audio file to text
    convert_audio_to_text(chosen_file_path)
