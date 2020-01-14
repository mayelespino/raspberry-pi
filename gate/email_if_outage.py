import smtplib, ssl
import os
from os import path
import requests

#
# Send email
# 
def send_email():
	port = 587  # For starttls
	smtp_server = os.environ.get('EMAIL_SERVER')
	sender_email = os.environ.get('EMAIL_FROM')
	receiver_email = os.environ.get('EMAIL_TO')
	password = os.environ.get('EMAIL_PASS')
	message = """\
	From: {0}
	Subject: There is an outage

	This message is sent from Python.""".format(sender_email)

	server=smtplib.SMTP(smtp_server, port) 
	server.starttls()
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message)
	server.close()

if __name__ == '__main__':
	emailWasSent = path.exists("/tmp/outage_email_sent.mem")
        sensorIsUp = True
	try:
		resp = requests.get('http://sensor.local')
		resp.raise_for_status()
	except:
		sensorIsUp = False

	if sensorIsUp is False and emailWasSent is False:
		open("/tmp/outage_email_sent.mem", 'a').close()
		send_email()
	elif sensorIsUp is True and emailWasSent is True:
		os.remove("/tmp/outage_email_sent.mem") 
	
#
# End
#
