#!/bin/bash
song=`ls -1 /var/www/mp3/sleep | xargs shuf -n1 -e`
/usr/bin/omxplayer /var/www/mp3/sleep/${song} > /dev/null 
