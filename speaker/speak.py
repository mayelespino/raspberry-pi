from gtts import gTTS
import os
import sys

if len(sys.argv) < 2:
    tts = gTTS(text='Hello!!', lang='en')
else:
    tts = gTTS(text=str(sys.argv[1]), lang='en')

tts.save("/tmp/tmp.mp3")
os.system("mplayer /tmp/tmp.mp3")
