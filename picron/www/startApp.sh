#!/bin/bash
cd /var/www/
nohup /usr/bin/python /var/www/run.py > /dev/null 2>&1&
ps aux | grep run.py |grep -v grep| awk '{print $2;}' > /var/run/picron.pid
nohup ngrok start -config=/var/www/ngrok.yml --all > /dev/null 2>&1&
pgrep ngrok > /var/run/ngrok.pid
