#!/bin/bash
touch /var/www/html/alarms.txt
chmod 777 /var/www/html/alarms.txt

cd /var/www/
nohup python /var/www/run.py  &
rm -f /var/www/alarm.pid
ps aux | grep run.py | grep -v grep | awk '{print $2;}' > /var/www/alarm.pid
