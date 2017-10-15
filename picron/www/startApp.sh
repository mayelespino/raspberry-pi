#!/bin/bash
cd /var/www/
nohup /usr/bin/python /var/www/run.py  &
ps aux | grep run.py |grep -v grep| awk '{print $2;}' > /var/run/picron.pid
