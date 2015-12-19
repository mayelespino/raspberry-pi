#!/bin/bash
cat << EOF > /home/pi/clock/clock.tab
# m h  dom mon dow   command
0 1 * * * /home/pi/clock/sync-clock.sh
0 1 * * * /home/pi/clock/update-crontab.sh
#-------
EOF
#
cat /home/pi/clock/d6ed3c7ed3e5b21bc0c9/clock.tab >> /home/pi/clock/clock.tab
/usr/bin/crontab /home/pi/clock/clock.tab
