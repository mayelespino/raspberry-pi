#!/usr/bin/python

import bluetooth
import datetime

result = bluetooth.lookup_name('DC:0C:5C:A1:14:6B', timeout=5)
currentDT = datetime.datetime.now()
if (result != None):
    with open('/mnt/ramdisk/bluetooth-stamp.txt', 'w') as sensorFile:
        sensorFile.write("%s-%s-%s %s:%s:%s\n" % (currentDT.day, currentDT.month, currentDT.year, currentDT.hour, currentDT.minute, currentDT.second))
    with open('/mnt/ramdisk/bluetooth-status.txt', 'w') as sensorFile:
        sensorFile.write("IN")
else:
    with open('/mnt/ramdisk/bluetooth-status.txt', 'w') as sensorFile:
        sensorFile.write("out")

