import smtplib, ssl
import os

#
# Send email
# 
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

#
# End
#
