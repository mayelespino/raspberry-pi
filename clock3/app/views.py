from app import app
import datetime
from pytz import timezone
from flask import request, session
from subprocess import call
from crontab import CronTab


#
# Common
#
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

@app.route('/cron', methods=['GET'])
def doGet():
    cron  = CronTab(user=True)
    returnString = ""
    for line in cron.lines:
        returnString = '%s%s\n' % (returnString, line)
    return returnString

@app.route('/cron/', methods=['DELETE'])
def clearCron():
    call(["crontab", "-r"])
    cron  = CronTab(user=True)
    cron_job = cron.new("/var/www/resync.sh")
    cron_job.every_reboot()
    cron_job.enable()
    cron.write()
    return "Alarms cleared!\n"

@app.route('/mute', methods=['POST'])
def mute():
    call(["killall", "/usr/bin/omxplayer.bin"])
    return "mute all playing now.\n"

#
# Sleep
#
@app.route('/sleep/daily/<time>', methods=['POST'])
def sleepDaily(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/var/www/sleep.sh')
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "sleep daily at ["+time+"] added.\n"

@app.route('/sleep/weekday/<time>', methods=['POST'])
def sleepWeekday(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/var/www/sleep.sh')
    cron_job.dow.on(1,2,3,4,5)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "sleep weekday at ["+time+"] added.\n"

@app.route('/sleep/now/', methods=['POST'])
def sleepNow():
    call(["/var/www/sleep.sh"])
    return "sleep playing now.\n"

#
# Wake Up
#
@app.route('/wakeup/daily/<time>', methods=['POST'])
def wakeupDaily(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/var/www/wakeup.sh')
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "wakeup daily at ["+time+"] added.\n"

@app.route('/wakeup/weekday/<time>', methods=['POST'])
def wakeupWeekday(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/var/www/sleep.sh')
    cron_job.dow.on(1,2,3,4,5)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "wakeup weekdays at ["+time+"] added.\n"

@app.route('/wakeup/now/', methods=['POST'])
def wakeupNow():
    call(["/var/www/wakeup.sh"])
    return "alarm playing now.\n"

@app.route('/muteall/now/', methods=['POST'])
def muteAllNow():
    call(["/var/www/muteAll.sh"])
    return "mute all now.\n"

@app.route('/stream/dance/now/', methods=['POST'])
def streamDanceNow():
    call(["/var/www/streamDance.sh"])
    return "stream dance now.\n"

@app.route('/stream/sleep/now/', methods=['POST'])
def streamSleepNow():
    call(["/var/www/streamSleep.sh"])
    return "stream sleep now.\n"

@app.route('/stream/npr/now/', methods=['POST'])
def streamNprNow():
    call(["/var/www/streamNPR.sh"])
    return "stream NPR now.\n"

@app.route('/stream/cristiana/now/', methods=['POST'])
def streamCristianaNow():
    call(["/var/www/streamCristiana.sh"])
    return "stream cristiana now.\n"

@app.route('/stream/news/now/', methods=['POST'])
def streamNewsNow():
    call(["/var/www/streamNews.sh"])
    return "stream news now.\n"

# EOF