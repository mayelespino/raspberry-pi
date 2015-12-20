from crontab import CronTab
 
#tab = CronTab(user='pi')
# tab.clear()
# tab.write()
# tab.close()
tab = CronTab(user='pi', tabfile='/usr/bin/python /home/pi/DEV/raspberry-pi/clock/clock-tab/clock.tab')
tab.write()
