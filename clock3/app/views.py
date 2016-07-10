from app import app
import datetime
from pytz import timezone
from flask import request, session
from subprocess import call

@app.route('/')
@app.route('/index')
def index():
    now = datetime.datetime.now(timezone('US/Pacific'))
    hour24 = now.hour
    if hour24 > 12 :
        hour = hour24 - 12
        ampm = 'PM'
    else: 
        hour = hour24
        ampm = 'AM'
    timeString = '[{}/{}/{} {}:{} {}]\n'.format(now.day,now.month,now.year,hour,now.minute,ampm)
    return timeString
        
@app.route('/alarms/', methods=['GET'])
def doGet():
    with open ("/var/www/alarms.txt", "r") as myfile:
        data="".join(line for line in myfile)
    return data

@app.route('/alarms/<alarm>', methods=['POST'])
def addAlarmDefault(alarm):
    writeCronFile(alarm)
    return alarm+"\n"

@app.route('/alarms/<alarm>/<days>', methods=['POST'])
def addAlarmParams(alarm,days):
    writeCronFile(alarm,days)
    return alarm+" "+days+"\n"

def writeCronFile(alarm,days=None):
    if ':' in alarm:
        (hour, minute) = alarm.split(":")
    else:
        hour = alarm
        minute = "00"
        
    if days is None:
        days = "*"
        
    if minute is None:
        minute = "*"
        
    line = "{} {} * * {} /var/www/alarm.sh\n".format(minute,hour,days)
    with open ("/var/www/alarms.txt", "a") as myfile:
        myfile.write(line)

@app.route('/alarms/', methods=['DELETE'])
def clearAlarms():
    with open ("/var/www/alarms.txt", "w") as myfile:
        line = "# m h  dom mon dow   command\n"
        myfile.write(line)
    call(["/usr/bin/crontab", "-r"])
    return "Alarms cleared!\n"

@app.route('/alarms/reload/', methods=['POST'])
def reloadCron():
    call(["/usr/bin/crontab", "-r"])
    call(["/usr/bin/crontab", "/var/www/alarms.txt"])
    return "alarm crontab reloaded\n"
#   
# EXAMPLES OF CURL COMMANDS TO BE USED
#
# curl -X POST http://localhost:5000/alarms/9:00
# curl -X GET http://localhost:5000/alarms/
# curl -X GET http://localhost:5000/
# curl -X DELETE http://localhost:5000/alarms/
        
        