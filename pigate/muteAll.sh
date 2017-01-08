#!/bin/bash

logger -i -t ${0} "Mute, received request from: ${1}"
result=`curl -X POST http://picron.local:5000/mute`
if [ ! -z "${1}" ]; then
  echo "${result}" | mail -s "mute reply" "${1}"  -a "From: pi@mayel.info"
fi
