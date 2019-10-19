from app import app
import datetime
from pytz import timezone
from flask import request, session
from subprocess import call
from subprocess import check_output
from crontab import CronTab
import pyttsx

#
#
#
stations = {}
stations['npr'] = 'https://nis.stream.publicradio.org/nis.mp3'
stations['nature01'] = 'http://66.55.145.43:7051/'
stations['nature02'] = 'http://192.240.102.198:14244/'
stations['nature03'] = 'http://209.126.119.76:8200/'
stations['chill01'] = 'http://uk2.internet-radio.com:31491/'
stations['chill02'] = 'http://radio.stereoscenic.com/asp-s'
stations['chill03'] = 'http://q2stream.wqxr.org/q2'
stations['chill04'] = 'http://stream2.mpegradio.com:8070/'
stations['logos01'] = 'http://14223.live.streamtheworld.com:80/WFFHFM_SC'
stations['logos02'] = 'http://18543.live.streamtheworld.com/FAMILYRADIO_WESTAAC_SC'
stations['logos03'] = 'http://ic2.christiannetcast.com/kver-fm'
stations['logos04'] = 'http://144.217.195.24:8992'
stations['dance01'] = 'http://pulseedm.cdnstream1.com:8124/1373_128'
stations['esp01'] = 'http://peridot.streamguys.com:5620/kdna-mp3'
stations['esp02'] = 'http://198.105.218.124:8200/'
stations['esp03'] = 'http://173.193.205.96:7055/stream'
stations['esp04'] = 'http://server10.servistreaming.com:9011/'
stations['talk01'] = 'http://provisioning.streamtheworld.com/pls/KCBSAM.pls'
stations['talk02'] = 'http://142.4.217.133:9195'
stations['talk03'] = 'http://176.31.98.109:4962'
stations['talk04'] = 'http://167.114.64.181:8462'
stations['talk05'] = 'http://netcast.kfjc.org/kfjc-192k-aac'
stations['talk06'] = 'https://icecastle.csumb.edu/live128'
stations['wakeup'] = stations['nature01']
stations['sleep'] = stations['nature02']
#
# 
#
@app.route('/')
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

@app.route('/help/', methods=['GET'])
def help():
    usage = """
    <pre>
@app.route('/')
@app.route('/help/', methods=['GET'])
@app.route('/cron/', methods=['GET'])
@app.route('/cron/', methods=['DELETE'])
@app.route('/cron/at/boot/', methods=['POST'])
@app.route('/volume/down/<number>/', methods=['POST'])
@app.route('/volume/up/<number>/', methods=['POST'])
@app.route('/mute/', methods=['POST'])
@app.route('/mute/<minutes>/minutes/', methods=['POST'])
@app.route('/play/<station>/', methods=['POST'])
@app.route('/stations/', methods=['GET'])
@app.route('/nowplaying/', methods=['GET'])
@app.route('/sleep/daily/<time>/', methods=['POST'])
@app.route('/sleep/wd/<time>/', methods=['POST'])
@app.route('/wakeup/daily/<time>/', methods=['POST'])
@app.route('/wakeup/wd/<time>/', methods=['POST'])
@app.route('/mute/daily/<time>/', methods=['POST'])
@app.route('/mute/we/<time>/', methods=['POST'])
@app.route('/mute/wd/<time>/', methods=['POST'])
@app.route('/sleep/', methods=['POST'])
@app.route('/wakeup/', methods=['POST'])
@app.route('/say/time/', methods=['POST'])
@app.route('/say/this_string/', methods=['POST'])
    </pre>
    """
    return usage

@app.route('/cron/', methods=['GET'])
def getCron():
    cron  = CronTab(user=True)
    cronString = "\n"
    for line in cron.lines:
        cronString  = '%s%s\n' % (cronString, line)
    returnString = "<pre>{}</pre>".format(cronString)
    return returnString

@app.route('/cron/', methods=['DELETE'])
def clearCron():
    cron  = CronTab(user=True)
    cron_job = cron.clear()
    cron_job.enable()
    cron.write()


@app.route('/cron/at/boot/', methods=['POST'])
def atBootCron():
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/sbin/service ntp restart',comment='Make sure the time is in sync.',user=True)
    cron_job.every_reboot()
    cron_job.enable()
    cron.write()
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
    return "mute\n"

#
# List stations and play a station now
#
@app.route('/play/<station>/', methods=['POST'])
def stationNow(station):
    if station not in stations:
        return "Invalid selection: {}\n".format(station)

    call(['mpc', 'clear'])
    call(['mpc', 'add', stations[station]])
    call(['mpc', 'play'])
    return "{} playing now.\n".format(station)

@app.route('/stations/', methods=['GET'])
def getStations():
    stations_string = ", ".join(stations.keys())
    return stations_string + "\n"

@app.route('/nowplaying/', methods=['GET'])
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
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/sleep/')
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "sleep daily at ["+time+"] added.\n"

@app.route('/sleep/we/<time>/', methods=['POST'])
def sleepWeekend(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/sleep/')
    cron_job.dow.on(0,6)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "sleep weekday at ["+time+"] added.\n"

@app.route('/sleep/wd/<time>/', methods=['POST'])
def sleepWeekday(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/sleep/')
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
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/wakeup/')
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "wakeup daily at ["+time+"] added.\n"

@app.route('/wakeup/we/<time>/', methods=['POST'])
def wakeupWeekend(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/wakeup/')
    cron_job.dow.on(0,6)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "wakeup weekdays at ["+time+"] added.\n"

@app.route('/wakeup/wd/<time>/', methods=['POST'])
def wakeupWeekday(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/wakeup/')
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

@app.route('/mute/we/<time>/', methods=['POST'])
def muteWeekend(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/wakeup/')
    cron_job.dow.on(0,6)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "mute weekend at ["+time+"] added.\n"

@app.route('/mute/wd/<time>/', methods=['POST'])
def muteWeekday(time):
    if ':' in time:
        (hour, minute) = time.split(":")
    else:
        hour = time
        minute = "00"
    cron  = CronTab(user=True)
    cron_job = cron.new(command='/usr/bin/curl -X POST http://localhost:5000/wakeup/')
    cron_job.dow.on(1,2,3,4,5)
    cron_job.hour.on(hour)
    cron_job.minute.on(minute)
    cron_job.enable()
    cron.write()
    return "wakeup weekdays at ["+time+"] added.\n"

#
# Sleep and Wake up 
#
@app.route('/sleep/', methods=['POST'])
def sleepNow():
    call(['mpc', 'clear'])
    call(['mpc', 'add', stations['sleep'] ])
    call(['mpc', 'play'])
    return "stream sleep now.\n"

@app.route('/wakeup/', methods=['POST'])
def wakeupNow():
    call(['mpc', 'clear'])
    call(['mpc', 'add', stations['wakeup'] ])
    call(['mpc', 'play'])
    return "stream wakeup now.\n"

#
# Say
#
@app.route('/say/time/', methods=['POST'])
def sayTimeNow():
    engine = pyttsx.init()
    engine.setProperty('rate', 55)
    time_now = datetime.datetime.now().strftime('%I:%M')
    time_text = "The time now is ..."
    engine.say(time_text)
    engine.say(time_now)
    engine.say("..")
    engine.say(time_now)
    engine.runAndWait()
    return "Say time now.\n"

@app.route('/say/<this_string>/', methods=['POST'])
def sayThisString(this_string):
    engine = pyttsx.init()
    engine.setProperty('rate', 55)
    engine.say(this_string)
    engine.runAndWait()
    return "Say string.\n"
###########
# EOF
###########
