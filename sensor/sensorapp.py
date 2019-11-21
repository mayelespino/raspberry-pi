from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'OK'

@app.route('/human/')
def human_sensor():
    with open('/mnt/ramdisk/sensor-human.txt','r') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
