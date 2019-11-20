import smbus
import datetime
import time

DEVICE_BUS = 1
DEVICE_ADDR = 0x17

TEMP_REG = 0x01
LIGHT_REG_L = 0x02
LIGHT_REG_H = 0x03
STATUS_REG = 0x04
ON_BOARD_TEMP_REG = 0x05
ON_BOARD_HUMIDITY_REG = 0x06
ON_BOARD_SENSOR_ERROR = 0x07
BMP280_TEMP_REG = 0x08
BMP280_PRESSURE_REG_L = 0x09
BMP280_PRESSURE_REG_M = 0x0A
BMP280_PRESSURE_REG_H = 0x0B
BMP280_STATUS = 0x0C
HUMAN_DETECT = 0x0D

bus = smbus.SMBus(DEVICE_BUS)

aReceiveBuf = []

aReceiveBuf.append(0x00) 

while True:
	bus = smbus.SMBus(DEVICE_BUS)
	for i in range(TEMP_REG,HUMAN_DETECT + 1):
    		aReceiveBuf.append(bus.read_byte_data(DEVICE_ADDR, i))

	if aReceiveBuf[HUMAN_DETECT] == 1 :
		    currentDT = datetime.datetime.now()
		    print("%s-%s-%s %s:%s:%s" % (currentDT.day, currentDT.month, currentDT.year, currentDT.hour, currentDT.minute, currentDT.second))
	time.sleep(3)
	print(".")
