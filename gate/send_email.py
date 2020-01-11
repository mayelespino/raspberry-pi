import smtplib, ssl
import os,sys

#
# Send email
# 
port = 587  # For starttls
smtp_server = os.environ.get('EMAIL_SERVER')
sender_email = os.environ.get('EMAIL_FROM')
receiver_email = os.environ.get('EMAIL_TO')
password = os.environ.get('EMAIL_PASS')
if len(sys.argv) < 2:
  subject = "Hi"
else:
  subject = sys.argv[1]

message = """\
From: {0}
Subject: {1}

This message is sent from Python.""".format(sender_email, subject)

server=smtplib.SMTP(smtp_server, port) 
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.close()

#
# End
#
