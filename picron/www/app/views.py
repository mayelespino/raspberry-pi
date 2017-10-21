from app import app
import datetime
from pytz import timezone
from flask import request, session
from subprocess import call
from subprocess import check_output
from crontab import CronTab
#
#
#
#sleep_stream_uri = 'http://mp3channels.webradio.antenne.de/chillout'
#sleep_stream_uri = 'http://sl128.hnux.com'
#sleep_stream_uri = 'http://radio.stereoscenic.com/asp-s'
#relax_stream_uri = 'http://radio.nolife-radio.com:9000/stream'
#dance_stream_uri = 'http://stream.dancewave.online:8080/dance.mp3'
#dance_stream_uri = 'http://pulseedm.cdnstream1.com:8124/1373_128'
#npr_stream_uri = 'https://nis.stream.publicradio.org/nis.mp3'
#logos_stream_uri = 'http://188.165.240.90:8193'
#logos_stream_uri = 'http://14223.live.streamtheworld.com:80/WFFHFM_SC'
#clasic_stream_uri = 'http://cms.stream.publicradio.org/cms.mp3'
#clasic_stream_uri = 'http://q2stream.wqxr.org/q2'
#nature_stream_uri = ''
#alt_stream_uri = 'http://stream2.mpegradio.com:8070/'
#dj_stram_uri='http://151.80.108.126:9530'
stations = {}
stations['sleep'] = 'http://radio.stereoscenic.com/asp-s'
stations['relax'] = 'http://radio.nolife-radio.com:9000/stream'
stations['dance'] = 'http://pulseedm.cdnstream1.com:8124/1373_128'
stations['npr'] = 'https://nis.stream.publicradio.org/nis.mp3'
stations['logos'] = 'http://14223.live.streamtheworld.com:80/WFFHFM_SC'
stations['classic'] = 'http://q2stream.wqxr.org/q2'
stations['alt'] = 'http://stream2.mpegradio.com:8070/'
stations['wake'] = 'http://q2stream.wqxr.org/q2'
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
# Volume 
#
@app.route('/volume/down/<number>/', methods=['POST'])
def volumeDown(number):
    call(['mpc', 'volume', '-{}'.format(number)])
    return "volume down {}.\n".format(number)

@app.route('/volume/up/<number>/', methods=['POST'])
def volumeUp(number):
    call(['mpc', 'volume', '+{}'.format(number)])
    return "volume up {}.\n".format(number)

#
# Mute
#
@app.route('/mute/', methods=['POST'])
def mute():
    call(['mpc', 'clear'])
    return "mute now.\n"

@app.route('/mute/<minutes>/minutes/', methods=['POST'])
def muteIn(minutes):
    call(['/var/www/muteAt.sh', minutes])
    return "mute in {} minutes.\n".format(minutes)

#
# List stations and play a station now
#
@app.route('/play/<station>/now/', methods=['POST'])
def stationNow(station):
    if station not in stations:
        return "Invalid selection: {}\n".format(station)

    call(['mpc', 'add', stations[station]])
    call(['mpc', 'play'])
    return "{} playing now.\n".format(station)

@app.route('/stations/', methods=['GET'])
def getStations():
    stations_string = ", ".join(stations.keys())
    return stations_string + "\n"

@app.route('/now/playing/', methods=['GET'])
def nowPlaying():
    status = check_output(["mpc", "current"])
    if status == "":
        status = "Nothing is playing now.\n"
    return status 

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
# Sleep and Wake up 
#
@app.route('/sleep/now/', methods=['POST'])
def sleepNow():
    call(['mpc', 'add', stations['sleep'] ])
    call(['mpc', 'play'])
    return "stream sleep now.\n"

@app.route('/wakeup/now/', methods=['POST'])
def wakeupNow():
    call(['mpc', 'add', stations['sleep'] ])
    call(['mpc', 'play'])
    return "stream wakeup now.\n"

###########
# EOF
###########
