from app import app
import datetime
from pytz import timezone
from flask import request, session
from subprocess import call
from crontab import CronTab
#
#
#
#sleep_stream_uri = 'http://mp3channels.webradio.antenne.de/chillout'
#sleep_stream_uri = 'http://sl128.hnux.com'
sleep_stream_uri = 'http://radio.stereoscenic.com/asp-s'
relax_stream_uri = 'http://radio.nolife-radio.com:9000/stream'
#dance_stream_uri = 'http://stream.dancewave.online:8080/dance.mp3'
dance_stream_uri = 'http://pulseedm.cdnstream1.com:8124/1373_128'
npr_stream_uri = 'https://nis.stream.publicradio.org/nis.mp3'
#logos_stream_uri = 'http://188.165.240.90:8193'
logos_stream_uri = 'http://14223.live.streamtheworld.com:80/WFFHFM_SC'
#clasic_stream_uri = 'http://cms.stream.publicradio.org/cms.mp3'
clasic_stream_uri = 'http://q2stream.wqxr.org/q2'
nature_stream_uri = ''
alt_stream_uri = 'http://stream2.mpegradio.com:8070/'
dj_stram_uri='http://151.80.108.126:9530'
#
# 
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

@app.route('/cron/', methods=['GET'])
def doGet():
    cron  = CronTab(user=True)
    returnString = ""
    for line in cron.lines:
        returnString = '%s%s\n' % (returnString, line)
    return returnString

@app.route('/cron/', methods=['DELETE'])
def clearCron():
    cron  = CronTab(user=True)
    cron_job = cron.clear()
    cron_job.enable()
    cron.write()
    ntp_cron = cron.new(command='/usr/sbin/service ntp restart',comment='Make sure the time is in sync.',user=True)
    ntp_cron.every_reboot()
    ntp_cron.enable()
    ntp_cron.write()
    return "Alarms cleared!\n"

#
# Volume and Mute
#
@app.route('/volume/down/<number>/', methods=['POST'])
def volumeDown(number):
    call(['mpc', 'volume', '-{}'.format(number)])
    return "volume down {}.\n".format(number)

@app.route('/volume/up/<number>/', methods=['POST'])
def volumeUp(number):
    call(['mpc', 'volume', '+{}'.format(number)])
    return "volume up {}.\n".format(number)

@app.route('/mute/', methods=['POST'])
def mute():
    call(['mpc', 'clear'])
    return "mute all now.\n"

#
# Sleep Cron
#
@app.route('/sleep/daily/<time>/', methods=['POST'])
def sleepDaily(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/sleep/now/')
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "sleep daily at ["+time+"] added.\n"

@app.route('/sleep/weekday/<time>/', methods=['POST'])
def sleepWeekday(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/sleep/now/')
    cron_job.dow.on(1,2,3,4,5)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "sleep weekday at ["+time+"] added.\n"

#
# WakeUp Cron
#
@app.route('/wakeup/daily/<time>/', methods=['POST'])
def wakeupDaily(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/wakeup/now/')
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "wakeup daily at ["+time+"] added.\n"

@app.route('/wakeup/weekday/<time>/', methods=['POST'])
def wakeupWeekday(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/wakeup/now/')
    cron_job.dow.on(1,2,3,4,5)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "wakeup weekdays at ["+time+"] added.\n"

#
# Mute Cron
#
@app.route('/mute/daily/<time>/', methods=['POST'])
def muteDaily(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/mute/')
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "mute daily at ["+time+"] added.\n"

@app.route('/wakeup/weekday/<time>/', methods=['POST'])
def muteWeekday(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/wakeup/now/')
    cron_job.dow.on(1,2,3,4,5)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "wakeup weekdays at ["+time+"] added.\n"

#
# Play Now
#
@app.route('/sleep/now/', methods=['POST'])
def sleepNow():
    call(['mpc', 'add', sleep_stream_uri])
    call(['mpc', 'play'])
    return "stream sleep now.\n"

@app.route('/wakeup/now/', methods=['POST'])
def wakeupNow():
    call(['mpc', 'add', relax_stream_uri])
    call(['mpc', 'play'])
    return "stream wakeup now.\n"

@app.route('/dance/now/', methods=['POST'])
def danceNow():
    call(['mpc', 'add', dance_stream_uri])
    call(['mpc', 'play'])
    return "stream dance now.\n"

@app.route('/npr/now/', methods=['POST'])
def nprNow():
    call(['mpc', 'add', npr_stream_uri])
    call(['mpc', 'play'])
    return "stream NPR now.\n"

@app.route('/logos/now/', methods=['POST'])
def logosNow():
    call(['mpc', 'add', logos_stream_uri])
    call(['mpc', 'play'])
    return "stream logos now.\n"

@app.route('/relax/now/', methods=['POST'])
def relaxNow():
    call(['mpc', 'add', relax_stream_uri])
    call(['mpc', 'play'])
    return "stream relax now.\n"

@app.route('/noise/now/', methods=['POST'])
def noiseNow():
    call(['mpc', 'add', noise_stream_uri])
    call(['mpc', 'play'])
    return "stream dance now.\n"

@app.route('/classic/now/', methods=['POST'])
def classicNow():
    call(['mpc', 'add', classic_stream_uri])
    call(['mpc', 'play'])
    return "stream classic now.\n"

@app.route('/nature/now/', methods=['POST'])
def natureNow():
    call(['mpc', 'add', nature_stream_uri])
    call(['mpc', 'play'])
    return "stream nature now.\n"

# EOF
