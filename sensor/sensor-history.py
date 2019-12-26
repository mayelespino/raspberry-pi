import os
from datetime import datetime

tempFileName = '/mnt/ramdisk/temperature.txt'
tempHistoryFileName = '/mnt/ramdisk/temperature-history.txt'

atHomeFileName = '/mnt/ramdisk/bluetooth-status.txt'
atHomeHistoryFileName = '/mnt/ramdisk/bluetooth-history.txt'

historySize = 24

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#
#
#
fullTempLine = ""
with open(tempFileName, 'r') as tf:
  temperature = tf.read()
  tokens = temperature.split()
  tempInt = int(tokens[0])
  tempFarenheit = tempInt * 1.8 + 32
  tempLine = "*" * tempInt
  fullTempLine = dt_string + " [" + tokens[0] + " C / " + str(tempFarenheit) + " F] " + tempLine 

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
#
#
#
fullAtHomeLine = ""
with open(atHomeFileName, 'r') as hf:
  atHome = hf.read()
  fullAtHomeLine = dt_string + " " + atHome 

if not os.path.exists(atHomeHistoryFileName):
    with open(atHomeHistoryFileName, 'w'): pass

historyLines = ""
with open(atHomeHistoryFileName, 'r') as hf:
  historyLines =  hf.readlines()
  historyLines = [x.strip() for x in historyLines] 

historyLines.append(fullAtHomeLine)

if len(historyLines) > historySize:
  historyLines = historyLines[1:]

with open(atHomeHistoryFileName, 'w') as hf:
  for line in historyLines:
    hf.write(line+'\n')
#
