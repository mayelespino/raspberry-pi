#!/bin/bash
echo "1)update"
sudo apt-get update
echo "2)apache2"
sudo apt-get install -y apache2
echo "3)python-pip"
sudo apt-get install -y python-pip
sudo apt-get install -y python-dev
sudo apt-get install -y build-essential
echo "4)flask"
sudo apt-get install -y flask
sudo pip install flask
echo "5)pytz"
sudo pip install pytz
echo "6)omxplayer"
sudo apt-get install omxplayer
#
echo "7)/var/www/app"
#sudo mkdir -p /var/www/app
sudo cp -R app /var/www/
sudo chmod -R 775 /var/www/app
echo "8)/var/www/mp3"
sudo mkdir -p /var/www/mp3
sudo chmod 775 /var/www/mp3 
sudo cp ../mp3s /var/www/mp3/
#
echo "9)alarms flask app"
sudo cp run.py /var/www/
sudo chmod +x /var/www/run.py
sudo touch /var/www/alarms.txt
sudo chmod 755 /var/www/alarms.txt
#
echo "index"
sudo cp index.html /var/www/html/
#
sudo cp {run.py,alarm.sh,resync.sh} /var/www/
sudo chmod +x /var/www/{run.py,alarm.sh,resync.sh}


