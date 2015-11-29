from crontab import CronTab
 
#tab = CronTab(user='pi',fake_tab='True')
tab = CronTab(user='pi')
cmd = '/usr/bin/python /home/pi/DEV/raspberry-pi/clock/playMP3.py'
cron_job = tab.new(cmd)
cron_job.setall('15 * * * *')
tab.write()
print tab.render()
