#!/bin/bash
kill -9 `cat /var/www/alarm.pid`
rm -f /var/www/alarm.pid
rm -f /var/www/nohup.out
