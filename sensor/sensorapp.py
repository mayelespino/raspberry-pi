from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'OK'

@app.route('/human/')
def human_sensor():
    with open('/mnt/ramdisk/human.txt','r') as f:
        data = f.read()
    return data

@app.route('/barometer/')
def barometer_sensor():
    with open('/mnt/ramdisk/barometer.txt','r') as f:
        data = f.read()
    return data

@app.route('/brightness/')
def brightness_sensor():
    with open('/mnt/ramdisk/brightness.txt','r') as f:
        data = f.read()
    return data

@app.route('/humidity/')
def humidity_sensor():
    with open('/mnt/ramdisk/humidity.txt','r') as f:
        data = f.read()
    return data

@app.route('/temperature/')
def temperature_sensor():
    with open('/mnt/ramdisk/temperature.txt','r') as f:
        data = f.read()
    return data

@app.route('/onboard-temp/')
def onboard_temp():
    with open('/mnt/ramdisk/onboard-temp.txt','r') as f:
        data = f.read()
    return data

@app.route('/time-stamp/')
def time_stamp():
    with open('/mnt/ramdisk/time-stamp.txt','r') as f:
        data = f.read()
    return data

@app.route('/bt-stamp/')
def bt_stamp():
    with open('/mnt/ramdisk/bluetooth-stamp.txt','r') as f:
        data = f.read()
    return data

@app.route('/bt-status/')
def bt_status():
    with open('/mnt/ramdisk/bluetooth-status.txt','r') as f:
        data = f.read()
    return data
#
#
#
@app.route('/temp-history/')
def temp_history():
    with open('/mnt/ramdisk/temperature-history.txt','r') as f:
        data = f.read()
    return data

@app.route('/athome-history/')
def athome_history():
    with open('/mnt/ramdisk/bluetooth-history.txt','r') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
