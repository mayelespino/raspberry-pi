#!/bin/bash

logger -i -t ${0} "Help, received request from: ${1}"

mail -s "Help reply" "${1}"  -a "From: pi@mayel.info" << EOF
Send the following in the subject line:
help
  To get this screen
stream-npr
  To start streaming NPR
mute
  To stop all sound 
EOF
