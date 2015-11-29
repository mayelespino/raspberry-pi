from crontab import CronTab
 
tab = CronTab(user='pi',fake_tab='True')
cmd = '/usr/bin/python /home/pi/DEV/raspberry-pi/clock/playMP3.py'
cron_job = tab.new(cmd)
cron_job.minute().every(5)
tab.write()
print tab.render()