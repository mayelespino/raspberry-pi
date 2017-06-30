#!/bin/bash

sudo /sbin/ip -s -s neigh flush all >/dev/null
#/usr/bin/hcitool scan  > /dev/null
sleep 5
for i in {1..4}
do
	/usr/bin/fping -c1 -g  10.0.1.0/24 > /dev/null 2>&1
	sleep 5
done
DATE=`date`

/usr/sbin/arp -n | grep -i "70:48:0f:71:9e:c5" > /dev/null
if [ $? -eq 0 ]
then
	twidge lsrecent | head -1 | grep _1_ >/dev/null
	if [ $? -ne 0 ]
	then
        	twidge update "_1_ [${DATE}]"
	fi
else
	twidge lsrecent | head -1 | grep _0_ >/dev/null
        if [ $? -ne 0 ]
        then
                twidge update "_0_ [${DATE}]"
        fi
fi
