import pyttsx
from datetime import datetime
engine = pyttsx.init()
engine.setProperty('rate', 55)
time_now = datetime.now().strftime('%I:%M')
time_text = "The time now is ..."
engine.say(time_text)
engine.say(time_now)
engine.say("..")
engine.say(time_now)
engine.runAndWait()
