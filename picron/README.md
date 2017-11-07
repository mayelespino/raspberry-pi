# picron
![picron index](https://github.com/mayelespino/raspberry-pi/blob/master/picron/picron-html.png)

# curl commands
```
get current time
curl -X GET http://picron.local:5000/
http://picron.local:5000/

get list of all cron jobs
curl -X GET http://picron.local:5000/cron/
href="http://picron.local:5000/cron/

delete all cron jobs
curl -X DELETE http://picron.local:5000/cron/

mute anythig playing right now
curl -X DELETE http://picron.local:5000/mute

set a wake up time
curl -X POST http://picron.local:5000/wakeup/daily/6:00 
curl -X POST http://picron.local:5000/wakeup/weekday/6:00 
curl -X POST http://picron.local:5000/wakeup/now/ 

set a sleep time:
curl -X POST http://picron.local:5000/sleep/daily/6:00
curl -X POST http://picron.local:5000/sleep/weekday/6:00
curl -X POST http://picron.local:5000/sleep/now/

play now:
curl -X POST http://picron.local:5000/wakeup/now/
curl -X POST http://picron.local:5000/sleep/now/
curl -X POST http://picron.local:5000/npr/now/ 
curl -X POST http://picron.local:5000/logos/now/
curl -X POST http://picron.local:5000/news/now/


```
# Usefull links
* http://raspberrypi.stackexchange.com/questions/38025/disable-console-autologin-on-raspbian-jessie
* https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=112702

# Great tutorial on flask
* http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
* http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* http://stackoverflow.com/questions/10434599/how-can-i-get-the-whole-request-post-body-in-python-with-flask
* http://flask.pocoo.org/docs/0.11/quickstart/
http://blog.luisrei.com/articles/flaskrest.html

# How to build a REST Web API on a Raspberry PI in JavaScript
* http://www.robert-drummond.com/2013/05/08/how-to-build-a-restful-web-api-on-a-raspberry-pi-in-javascript-2/

# Turning Raspberry Pi into a web server
* http://www.chrisjmendez.com/2016/06/30/turning-raspberry-pi-into-a-web-server/

# Monit
* http://docs.ansible.com/ansible/latest/monit_module.html
* https://www.digitalocean.com/community/questions/monit-error-in-ubuntu

# misc
* http://stackoverflow.com/questions/2925230/get-235pm-instead-of-0235pm-from-python-date-time
* http://askubuntu.com/questions/254826/how-to-force-a-clock-update-using-ntp
* http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
* https://www.raspberrypi.org/documentation/linux/usage/cron.md
* https://www.pantz.org/software/cron/croninfo.html
* https://www.gaggl.com/2013/01/installing-omxplayer-on-raspberry-pi/
* http://www.raspberry-projects.com/pi/software_utilities/media-players/omxplayer
* https://www.raspberrypi.org/forums/viewtopic.php?f=51&t=45265
* https://learn.adafruit.com/running-programs-automatically-on-your-tiny-computer/systemd-writing-and-enabling-a-service

# javascript
* http://stackoverflow.com/questions/14563234/php-with-javascript-code-live-clock
* http://www.pratermade.com/2014/08/setting-up-your-raspberry-pi-environment/
* http://www.htmlgoodies.com/beyond/javascript/read-text-files-using-the-javascript-filereader.html#fbid=AMBhy7XR7d1

# additional installations
```
sudo pip install pytz
```

# system config
* http://askubuntu.com/questions/175751/how-do-i-run-a-python-script-in-the-background-and-restart-it-after-a-crash

# additional packages
- http://askubuntu.com/questions/339298/conveniently-schedule-a-command-to-run-later

# Ansible
* https://gist.github.com/muloka/7687250

# Ubuntu
* https://askubuntu.com/questions/187888/what-is-the-correct-way-to-completely-remove-an-application

# python crontab
* http://blog.appliedinformaticsinc.com/managing-cron-jobs-with-python-crontab/

# streaming audio
* http://www.instructables.com/id/Raspberry-Pi-Internet-Radio-With-Flask/
* https://www.internet-radio.com
* https://stackoverflow.com/questions/20460296/playing-remote-audio-files-in-python
* http://yodaconditional.blogspot.com/2013/05/playing-streaming-audio-with-python-and.html
* http://wiki.secondlife.com/wiki/Music_streams
* https://www.calmsound.com/rainforest
## Some specific stations, URLS
sleep_stream_uri = 'http://mp3channels.webradio.antenne.de/chillout'
sleep_stream_uri = 'http://sl128.hnux.com'
sleep_stream_uri = 'http://radio.stereoscenic.com/asp-s'
relax_stream_uri = 'http://radio.nolife-radio.com:9000/stream'
dance_stream_uri = 'http://stream.dancewave.online:8080/dance.mp3'
dance_stream_uri = 'http://pulseedm.cdnstream1.com:8124/1373_128'
npr_stream_uri = 'https://nis.stream.publicradio.org/nis.mp3'
logos_stream_uri = 'http://188.165.240.90:8193'
logos_stream_uri = 'http://14223.live.streamtheworld.com:80/WFFHFM_SC'
clasic_stream_uri = 'http://cms.stream.publicradio.org/cms.mp3'
clasic_stream_uri = 'http://q2stream.wqxr.org/q2'
nature_stream_uri = ''
alt_stream_uri = 'http://stream2.mpegradio.com:8070/'
dj_stram_uri='http://151.80.108.126:9530'

# to change the timezone to pacific
https://www.raspberrypi.org/forums/viewtopic.php?t=4977&f=5
```
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/US/Pacific /etc/localtime
sudo rm /etc/timezone
echo "US/Pacific" | sudo tee /etc/timezone 
```

# To do
- restart and get status for support services:
    - mpd
    - monit
- Reminders. Using text to speach. Have a rest api call to add reminders at a certain time and/or red off reminders from web page.
