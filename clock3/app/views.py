from app import app
import datetime
from pytz import timezone
from flask import request, session
from subprocess import call
from crontab import CronTab

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
    with open ("/var/www/html/alarms.txt", "r") as myfile:
        data="".join(line for line in myfile)
    return data

@app.route('/sleep/<time>', methods=['POST'])
def addSleepDefault(time):
    cron  = CronTab(user=True)
    job = cron.new(command='/var/www/sleep.sh')
    job.dow.on(1,2,3,4,5)
    job.hour.on(time)
    cron.write()
    cron.write('/var/www/html/cron.txt')
    return time+"\n"

@app.route('/alarms/<time>', methods=['POST'])
def addAlarmDefault(time):
    writeCronFile(time, None, "alarm")
    reloadCron()
    return time+"\n"

@app.route('/alarms/<time>/<days>', methods=['POST'])
def addAlarmParams(time, days, script="alarm"):
    writeCronFile(time,days, "sleep")
    reloadCron()
    return time+" "+days+"\n"

@app.route('/sleep/<time>/<days>', methods=['POST'])
def addSleepParams(time, days, script="sleep"):
    writeCronFile(time,days, "sleep")
    return time+" "+days+"\n"
    reloadCron()
def writeCronFile(time, days=None, script="alarm"):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"

    if days is None:
        days = "*"

    if minute is None:
        minute = "*"

    if script == 'sleep':
        line = "{} {} * * {} /var/www/sleep.sh\n".format(minute,hour,days)
    else:
        line = "{} {} * * {} /var/www/alarm.sh\n".format(minute,hour,days)

    with open ("/var/www/html/alarms.txt", "a") as myfile:
        myfile.write(line)

@app.route('/alarms/', methods=['DELETE'])
def clearAlarms():
    call(["/usr/bin/crontab", "-r"])
    with open ("/var/www/html/alarms.txt", "w") as myfile:
        cronFile = """@reboot /var/www/resync.sh\n@reboot /var/www/reload.sh\n# m h  dom mon dow   command\n"""
        myfile.write(cronFile)
    reloadCron()
    return "Alarms cleared!\n"

@app.route('/alarms/reload/', methods=['POST'])
def reloadCron():
    call(["/usr/bin/crontab", "-r"])
    call(["/usr/bin/crontab", "/var/www/html/alarms.txt"])
    return "alarm crontab reloaded\n"

@app.route('/sleep/playnow/', methods=['POST'])
def playSleepNow():
    call(["/var/www/sleep.sh"])
    return "sleep playing now.\n"

@app.route('/alarms/playnow/', methods=['POST'])
def playAlarmNow():
    call(["/var/www/alarm.sh"])
    return "alarm playing now.\n"
#
