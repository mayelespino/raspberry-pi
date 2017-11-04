import pyttsx
from datetime import datetime
engine = pyttsx.init()
engine.setProperty('rate', 55)
time_now = datetime.now().strftime('%I:%M')
engine.say(time_now)
engine.runAndWait()
