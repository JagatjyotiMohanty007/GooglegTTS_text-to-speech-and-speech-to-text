# Python Text-to-Speech and Speech-to-Text Project

This project demonstrates:

1. Text to Voice using gTTS (Google Text-to-Speech)
2. Voice to Text using SpeechRecognition

---

# Project Structure

```bash
project/
│
├── text_to_voice.py
├── voice_to_text.py
├── test_voice.mp3
└── README.md
```

---

# 1. Text to Voice using gTTS

## Install Required Package

```bash
pip install gtts
```

## Python Code

```python
from gtts import gTTS
import os

# Text to convert
text = "Hello Jagatjyoti, this is a test voice generated using gTTS."

# Language
language = 'en'

# Convert text to speech
speech = gTTS(text=text, lang=language, slow=False)

# Save audio file
speech.save("test_voice.mp3")

print("Voice file created successfully!")

# Play audio file
os.system("start test_voice.mp3")
```

---

## Supported Languages

| Language | Code |
|---|---|
| English | en |
| Hindi | hi |
| Telugu | te |
| Tamil | ta |

---

# 2. Voice to Text using SpeechRecognition

## Install Required Packages

```bash
pip install SpeechRecognition
pip install pyaudio
```

---

## If PyAudio Installation Fails on Windows

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Python Code

```python
import speech_recognition as sr

# Create recognizer
r = sr.Recognizer()

# Use microphone
with sr.Microphone() as source:
    print("Speak something...")

    # Listen to microphone
    audio = r.listen(source)

try:
    # Convert speech to text
    text = r.recognize_google(audio)

    print("You said:", text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Error:", e)
```

---

# Hindi Voice to Text

```python
text = r.recognize_google(audio, language='hi-IN')
print(text)
```

---

# Telugu Voice to Text

```python
text = r.recognize_google(audio, language='te-IN')
print(text)
```

---

# How It Works

## Text to Speech (gTTS)

1. Enter text
2. gTTS converts text into audio
3. Audio saved as MP3
4. MP3 file plays automatically

---

## Speech to Text

1. Microphone captures voice
2. SpeechRecognition processes audio
3. Google Speech API converts voice to text
4. Text displayed in console

---

# Run the Project

## Run Text to Voice

```bash
python text_to_voice.py
```

## Run Voice to Text

```bash
python voice_to_text.py
```

---

# Technologies Used

- Python
- gTTS
- SpeechRecognition
- PyAudio

---

# GitHub Commit Commands

```bash
git init
git add .
git commit -m "Added text to speech and speech to text project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_LINK
git push -u origin main
```

---

# Author

Jagatjyoti Mohanty
# Python Text-to-Speech and Speech-to-Text Project

This project demonstrates:

1. Text to Voice using gTTS (Google Text-to-Speech)
2. Voice to Text using SpeechRecognition

---

# Project Structure

```bash
project/
│
├── text_to_voice.py
├── voice_to_text.py
├── test_voice.mp3
└── README.md
```

---

# 1. Text to Voice using gTTS

## Install Required Package

```bash
pip install gtts
```

## Python Code

```python
from gtts import gTTS
import os

# Text to convert
text = "Hello Jagatjyoti, this is a test voice generated using gTTS."

# Language
language = 'en'

# Convert text to speech
speech = gTTS(text=text, lang=language, slow=False)

# Save audio file
speech.save("test_voice.mp3")

print("Voice file created successfully!")

# Play audio file
os.system("start test_voice.mp3")
```

---

## Supported Languages

| Language | Code |
|---|---|
| English | en |
| Hindi | hi |
| Telugu | te |
| Tamil | ta |

---

# 2. Voice to Text using SpeechRecognition

## Install Required Packages

```bash
pip install SpeechRecognition
pip install pyaudio
```

---

## If PyAudio Installation Fails on Windows

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Python Code

```python
import speech_recognition as sr

# Create recognizer
r = sr.Recognizer()

# Use microphone
with sr.Microphone() as source:
    print("Speak something...")

    # Listen to microphone
    audio = r.listen(source)

try:
    # Convert speech to text
    text = r.recognize_google(audio)

    print("You said:", text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Error:", e)
```

---

# Hindi Voice to Text

```python
text = r.recognize_google(audio, language='hi-IN')
print(text)
```

---

# Telugu Voice to Text

```python
text = r.recognize_google(audio, language='te-IN')
print(text)
```

---

# How It Works

## Text to Speech (gTTS)

1. Enter text
2. gTTS converts text into audio
3. Audio saved as MP3
4. MP3 file plays automatically

---

## Speech to Text

1. Microphone captures voice
2. SpeechRecognition processes audio
3. Google Speech API converts voice to text
4. Text displayed in console

---

# Run the Project

## Run Text to Voice

```bash
python text_to_voice.py
```

## Run Voice to Text

```bash
python voice_to_text.py
```

---

# Technologies Used

- Python
- gTTS
- SpeechRecognition
- PyAudio

---

# GitHub Commit Commands

```bash
git init
git add .
git commit -m "Added text to speech and speech to text project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_LINK
git push -u origin main
```

---

# Author

Jagatjyoti Mohanty
# Python Text-to-Speech and Speech-to-Text Project

This project demonstrates:

1. Text to Voice using gTTS (Google Text-to-Speech)
2. Voice to Text using SpeechRecognition

---

# Project Structure

```bash
project/
│
├── text_to_voice.py
├── voice_to_text.py
├── test_voice.mp3
└── README.md
```

---

# 1. Text to Voice using gTTS

## Install Required Package

```bash
pip install gtts
```

## Python Code

```python
from gtts import gTTS
import os

# Text to convert
text = "Hello Jagatjyoti, this is a test voice generated using gTTS."

# Language
language = 'en'

# Convert text to speech
speech = gTTS(text=text, lang=language, slow=False)

# Save audio file
speech.save("test_voice.mp3")

print("Voice file created successfully!")

# Play audio file
os.system("start test_voice.mp3")
```

---

## Supported Languages

| Language | Code |
|---|---|
| English | en |
| Hindi | hi |
| Telugu | te |
| Tamil | ta |

---

# 2. Voice to Text using SpeechRecognition

## Install Required Packages

```bash
pip install SpeechRecognition
pip install pyaudio
```

---

## If PyAudio Installation Fails on Windows

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Python Code

```python
import speech_recognition as sr

# Create recognizer
r = sr.Recognizer()

# Use microphone
with sr.Microphone() as source:
    print("Speak something...")

    # Listen to microphone
    audio = r.listen(source)

try:
    # Convert speech to text
    text = r.recognize_google(audio)

    print("You said:", text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Error:", e)
```

---

# Hindi Voice to Text

```python
text = r.recognize_google(audio, language='hi-IN')
print(text)
```

---

# Telugu Voice to Text

```python
text = r.recognize_google(audio, language='te-IN')
print(text)
```

---

# How It Works

## Text to Speech (gTTS)

1. Enter text
2. gTTS converts text into audio
3. Audio saved as MP3
4. MP3 file plays automatically

---

## Speech to Text

1. Microphone captures voice
2. SpeechRecognition processes audio
3. Google Speech API converts voice to text
4. Text displayed in console

---

# Run the Project

## Run Text to Voice

```bash
python text_to_voice.py
```

## Run Voice to Text

```bash
python voice_to_text.py
```

---

# Technologies Used

- Python
- gTTS
- SpeechRecognition
- PyAudio

---

# GitHub Commit Commands

```bash
git init
git add .
git commit -m "Added text to speech and speech to text project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_LINK
git push -u origin main
```

---

# Author

Jagatjyoti Mohanty
