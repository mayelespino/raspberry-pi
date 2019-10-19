#!/bin/bash

function processEmail { 

from=`grep "From: " ${1} | awk '{print $4;}' | tr -d \< | tr -d \>`
subject=`grep Subject: ${1} |awk '{print $2;}'`
subject="${subject^^}"

logger -i -t ${0} "from: ${from}"
logger -i -t ${0} "subject: ${subject}"

case "${subject}" in
  *TIME*)
    /home/pi/timeResponse.sh "$from"
    ;;
  *STREAM-CRISTIANA*)
    /home/pi/streamCristiana.sh "$from"
    ;;
  *STREAM-SLEEP*)
    /home/pi/streamSleep.sh "$from"
    ;;
  *STREAM-DANCE*)
    /home/pi/streamDance.sh "$from"
    ;;
  *STREAM-NEWS*)
    /home/pi/streamNews.sh "$from"
    ;;
  *STREAM-NPR*)
    /home/pi/streamNPR.sh "$from"
    ;;
  *MUTE*)
    /home/pi/muteAll.sh "$from"
    ;;
  *STATUS*)
    /home/pi/statusResponse.sh "$from"
    ;;
  *HELP*)
    /home/pi/helpResponse.sh "$from"
    ;;
  *)
    logger -i -t ${0} "not supported: ${subject}"
    ;;
esac

rm -f ${1}
}


logger -i -t ${0} "fetching email."
/usr/bin/fetchmail -a -F
sleep 2

for f in /home/pi/inbox/mail*
do 
  logger -i -t ${0} "procesing: ${f}"
  processEmail $f 
done
