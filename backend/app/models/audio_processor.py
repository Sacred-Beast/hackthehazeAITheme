# app/utils/audio_processor.py

import speech_recognition as sr
import tempfile
import os

def speech_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        return str(e)
