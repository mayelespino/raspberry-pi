from gtts import gTTS
import os
import sys

if len(sys.argv) < 2:
    tts = gTTS(text='Hola!', lang='es')
else:
    tts = gTTS(text=str(sys.argv[1]), lang='es')

tts.save("/mnt/ramdisk/tmp.mp3")
os.system("mplayer /mnt/ramdisk/tmp.mp3")
