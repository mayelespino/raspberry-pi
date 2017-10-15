#!/bin/bash
pkill -f "python /var/www/run.py"
rm -f /var/www/nohup.out
rm -f /var/run/picron.pid
