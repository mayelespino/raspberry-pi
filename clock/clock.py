import time
from time import ctime
import datetime

clock_time = None
try:
    import ntplib
    server = 'pool.ntp.org'
    client = ntplib.NTPClient()
    response = client.request(server)
    localTime = response.tx_time
    localTime = localTime - 28800 #28800 is 8 hours
    print ctime(localTime)
    print time.localtime(localTime)
    #sudodate = subprocess.Popen(["sudo", "date", "-s", "Thu Aug  9 21:31:26 UTC 2012"])
    #sudodate.communicate()
except:
  print "Could not synch with server", server 
#except:
#  print "Error formating time."
print "Done"
