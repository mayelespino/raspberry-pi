#!/bin/bash

sudo apt-get update
sudo apt-get install -y apache2
sudo apt-get install -y python-pip
sudo apt-get install -y python-dev
sudo apt-get install -y build-essential
sudo apt-get install -y flask
sudo pip install flask
sudo apt-get install omxplayer
#
sudo mkdir -p /var/www/app
sudo cp -R app /var/www/app
sudo chmod -R 775 /var/www/app
sudo mkdir -p /var/www/mp3
sudo chmod 775 /var/www/mp3 
#
sudo cp run.py /var/www/
sudo chmod +x /var/www/run.py
sudo touch /var/www/alarms.txt
sudo chmod 755 /var/www/alarms.txt
#
sudo cp {run.py,alarm.sh,resync.sh} /var/www/
sudo chmod +x /var/www/{run.py,alarm.sh,resync.sh}


