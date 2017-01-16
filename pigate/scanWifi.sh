#!/bin/bash

fping -c1 -g  10.0.1.0/24 > /dev/null 2>&1

MAYELIPHONE=`arp -an | grep -i 70:48:0F:71:9E:C5`
DATE=`date`

if [ -n "${MAYELIPHONE}" ]
then
    if [ ! -e /tmp/iphone.home ]
    then
        touch /tmp/iphone.home
        twidge update "IN [${DATE}]"
    fi
else
    echo "GONE!"
    if [ -e /tmp/iphone.home ]
    then
        twidge update "OUT [${DATE}]"
        rm -f /tmp/iphone.home
    fi
fi
