from flask import Flask
import subprocess 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'OK'

@app.route('/mute/', methods=['POST'])
def play_mute():
    subprocess.Popen(["/usr/bin/pkill","mplayer","-c"])
    return "OK"

@app.route('/scanner/', methods=['POST'])
def play_scanner():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://198.178.123.20:10488/listen.pls"])
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://104.167.4.67:8296/listen.pls"])
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://162.244.80.118:9196/listen.pls"])
    return "OK"

@app.route('/nature/', methods=['POST'])
def play_nature():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://94.23.252.14:8067/listen.pls"])
    return "OK"

@app.route('/pink/', methods=['POST'])
def play_pink():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://uk1.internet-radio.com:8004/listen.pls"])
    return "OK"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
