#!/bin/bash
pkill -f "python /var/www/run.py"
pkill -f ngrok
rm -f /var/www/nohup.out
rm -f /var/run/picron.pid
rm -f /var/run/ngrok.pid
