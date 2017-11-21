#!/bin/bash

logger -i -t ${0} "Time, received request from: ${1}"

result=`curl -X GET http://picron.local:5000/`
echo "${result}" | mail -s "times reply" "${1}"  -a "From: pi@mayel.info"
