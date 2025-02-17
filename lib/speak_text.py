import os

from gtts import gTTS


def speak_text(text, filename="response.mp3"):
    filename = f'generate/{filename}'
    tts = gTTS(text=text, lang="th")
    tts.save(filename)
    os.system(f"afplay {filename}")
    