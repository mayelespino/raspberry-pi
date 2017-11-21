#!/bin/bash

logger -i -t ${0} "Status, received request from: ${1}"

time=`curl -X GET http://picron.local:5000/`
alarms=`curl -X GET http://picron.local:5000/cron`
pict=`crontab -l`
piup=`uptime`
pisyslog=`tail /var/log/syslog`

mail -s "Status reply" "${1}"  -a "From: pi@mayel.info" << EOF

Time in alarm clock:
${time}

Current cron tab in alarm:
${alarms}

Current crontab on pi@mayel.info (pi1):
${pict}

Uptime on pi@mayel.info:
${piup}

Tail of syslog on pi@mayel.info:
${pisyslog}
EOF
