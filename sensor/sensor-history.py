import os
from datetime import datetime

tempFileName = '/mnt/ramdisk/temperature.txt'
tempHistoryFileName = '/mnt/ramdisk/temperature-history.txt'
historySize = 24

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

fullTempLine = ""
with open(tempFileName, 'r') as tf:
  temperature = tf.read()
  tokens = temperature.split()
  tempInt = int(tokens[0])
  tempLine = "-" * tempInt
  fullTempLine = dt_string + "|" + temperature + "|" + tempLine + "|"

if not os.path.exists(tempHistoryFileName):
    with open(tempHistoryFileName, 'w'): pass

historyLines = ""
with open(tempHistoryFileName, 'r') as hf:
  historyLines =  hf.readlines()
  historyLines = [x.strip() for x in historyLines] 

historyLines.append(fullTempLine)

if len(historyLines) > historySize:
  historyLines = historyLines[1:]

with open(tempHistoryFileName, 'w') as hf:
  for line in historyLines:
    hf.write(line+'\n')
