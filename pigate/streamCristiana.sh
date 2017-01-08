#!/bin/bash

logger -i -t ${0} "Stream Cristiana, received request from: ${1}"

result=`curl -X POST http://picron.local:5000/stream/cristiana/now/`
if [ ! -z "${1}" ]; then
  echo "${result}" | mail -s "stream-npr reply" "${1}"  -a "From: pi@mayel.info"
fi
