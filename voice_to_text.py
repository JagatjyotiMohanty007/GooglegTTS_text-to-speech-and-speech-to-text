# pip install SpeechRecognition
# pip install pyaudio

# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr

# Create recognizer
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("Speak something...")
    
    # Read audio
    audio = r.listen(source)

try:
    # Convert voice to text using Google API
    text = r.recognize_google(audio)

    print("You said:", text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Error:", e)