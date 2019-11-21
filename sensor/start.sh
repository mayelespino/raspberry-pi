# export FLASK_APP=/home/pi/repo/sensor/sensorapp.py
# nohup flask run --host=0.0.0.0  >/dev/null 2>&1 &
#flask run --host=0.0.0.0 
nohup /usr/bin/python /home/pi/repo/sensor/sensorapp.py  >/dev/null 2>&1 &
nohup /home/pi/repo/sensor/sensor-human-loop.sh >/dev/null 2>&1 &
