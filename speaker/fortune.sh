#!/bin/bash
/usr/bin/curl -X POST http://speaker.local:5000/100/
/usr/bin/python /home/pi/repo/speaker/say.py "`fortune`" 
