#!/bin/bash 

cd /home/pi/DEV/raspberry-pi/clock/d6ed3c7ed3e5b21bc0c9/ && /usr/bin/git pull git@gist.github.com:d6ed3c7ed3e5b21bc0c9.git | grep "Already up-to-date."
if [ $? == 0 ]; then
    echo "Changed, updating cron"
else
    echo "NO CHAGE"
fi

