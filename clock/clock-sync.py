import time
from time import ctime
import subprocess

clock_time = None
try:
    import ntplib
    server = 'pool.ntp.org'
    client = ntplib.NTPClient()
    response = client.request(server)
    localTime = response.tx_time
    localTime = localTime - 28800 #28800 is 8 hours
    localTimeString= ctime(localTime)
    sudodate = subprocess.Popen(["sudo", "date", "-s", localTimeString])
    sudodate.communicate()
except:
  print "Could not synch with server"
