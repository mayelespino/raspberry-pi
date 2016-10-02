#!/bin/bash
song=`ls -1 /var/www/mp3s/wakeup | xargs shuf -n1 -e`
/usr/bin/omxplayer /var/www/mp3/wakeup/${song} > /dev/null
