import bluetooth
import time

while 1:
	if bluetooth.lookup_name('DC:0C:5C:A1:14:6B') == 'iPhone':
		print "Yes"
	else:
		print "No"
	time.sleep(1)
