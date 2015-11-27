import time
import os

try:
    import ntplib
    server = 'pool.ntp.org'
    client = ntplib.NTPClient()
    response = client.request(server)
    os.system('date' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
except:
  print "Could not synch with server", server 

print "Done"
