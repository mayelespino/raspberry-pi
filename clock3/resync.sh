#!/bin/bash
DTZ="US/Pacific"

/etc/init.d/ntp restart

grep "$DTZ" /etc/timezone >/dev/null
if [ "$?" -ne "0" ]
then
  echo "Reseting to ${DTZ}"
  echo "${DTZ}" > /etc/timezone
fi
#
# http://raspberrypi.stackexchange.com/questions/4370/where-does-the-raspberry-pi-get-the-time-from
# http://www.pool.ntp.org/en/use.html
#
# Replace the list of servers with the one you found in the webpage. e.g.
#
# vi /etc/ntp.conf
#server 0.pool.ntp.org
#server 1.pool.ntp.org
#server 2.pool.ntp.org
#server 3.pool.ntp.org
#
