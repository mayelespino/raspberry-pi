#!/bin/bash
echo "Before"
date
echo "Sync"
/usr/bin/python /home/pi/clock/clock-sync.py
echo "After"
date

