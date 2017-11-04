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
stations = {}
stations['sleep'] = 'http://66.55.145.43:7051/'
stations['nature'] = 'http://66.55.145.43:7051/'
stations['relax'] = 'http://uk5.internet-radio.com:8075/'
stations['chill'] = 'http://radio.stereoscenic.com/asp-s'
stations['dance'] = 'http://pulseedm.cdnstream1.com:8124/1373_128'
stations['npr'] = 'https://nis.stream.publicradio.org/nis.mp3'
stations['logos'] = 'http://14223.live.streamtheworld.com:80/WFFHFM_SC'
stations['classic'] = 'http://q2stream.wqxr.org/q2'
stations['alt'] = 'http://stream2.mpegradio.com:8070/'
stations['wake'] = 'http://198.105.218.124:8200/'
stations['house'] = 'http://uk3.internet-radio.com:8435/'
stations['instrumental'] = 'http://198.105.218.124:8200/'
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

@app.route('/help/', methods=['GET'])
def help():
    usage = """
    <pre>
    curl -X GET http://picron.local:5000/
    curl -X POST http://picron.local:5000/
    curl -X DELETE http://picron.local:5000/

    GET / .- Returns current time
    GET /cron/ .-  Returns current cron sttings.
    GET /stations/ .- Returns available stations.
    GET /now/playing/

    DELETE /cron/ .- Deletes all cron jobs

    POST /reboot/sync/ .- Add at boot time syncinstructions.
    POST /volume/down/<number>/
    POST /volume/up/<number>/
    POST /mute/
    POST /mute/<minutes>/minutes/
    POST /play/<station>/now/
    POST /sleep/daily/<time>/
    POST /sleep/weekday/<time>/
    POST /wakeup/daily/<time>/
    POST /wakeup/weekday/<time>/
    POST /mute/daily/<time>/
    POST /mute/weekday/<time>/
    POST /sleep/now/
    POST /wakeup/now/
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

@app.route('/mute/weekday/<time>/', methods=['POST'])
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
