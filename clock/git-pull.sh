cd /home/pi/DEV/raspberry-pi/clock/clock-tab
/usr/bin/git pull | grep "Already up-to-date"
if $? == 1 ]
  /usr/bin/crontab /home/pi/DEV/raspberry-pi/clock/clock-tab/clock.tab
fi
