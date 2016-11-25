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

@app.route('/cron/', methods=['GET'])
def doGet():
    cron  = CronTab(user=True)
    for line in cron.lines:
      print line
    return

@app.route('/cron/', methods=['DELETE'])
def clearCron():
    cron  = CronTab(user=True)
    cron.remove_all()
    return "Alarms cleared!\n"

@app.route('/sleep/daily/<time>', methods=['POST'])
def sleepDaily(time):
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/var/www/sleep.sh')
    cron_job.enable()
    cron_job.hour.on(time)
    cron.write()
    return "sleep daily at"+time+" added.\n"

@app.route('/sleep/weekday/<time>', methods=['POST'])
def sleepWeekday(time):
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/var/www/sleep.sh')
    cron_job.dow.on(1,2,3,4,5)
    cron_job.hour.on(time)
    cron_job.enable()
    cron.write()
    return "sleep weekday at"+time+" added.\n"

@app.route('/sleep/now/', methods=['POST'])
def sleepNow():
    call(["/var/www/sleep.sh"])
    return "sleep playing now.\n"

@app.route('/wakeup/daily/<time>', methods=['POST'])
def wakeupDaily(time):
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/var/www/wakeup.sh')
    cron_job.enable()
    cron_job.hour.on(time)
    cron.write()
    return "done\n"

@app.route('/wakeup/weekday/<time>', methods=['POST'])
def wakeupWeekday(time):
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/var/www/wakeup.sh')
    cron_job.dow.on(1,2,3,4,5)
    cron_job.hour.on(time)
    cron_job.enable()
    cron.write()
    return "done\n"

@app.route('/wakeup/now/', methods=['POST'])
def playAlarmNow():
    call(["/var/www/alarm.sh"])
    return "alarm playing now.\n"
#
