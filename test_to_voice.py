 # pip install gtts
 
from gtts import gTTS
import os

# Text to convert
text = "Hello Jagatjyoti, this is a test voice generated using gTTS."

# Language
language = 'en'

# Create gTTS object
speech = gTTS(text=text, lang=language, slow=False)

# Save audio file
speech.save("test_voice.mp3")

print("Voice file created successfully!")

# Play the audio file (Windows)
os.system("start test_voice.mp3")