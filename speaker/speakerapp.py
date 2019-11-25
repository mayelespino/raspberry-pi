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

@app.route('/bible/', methods=['POST'])
def play_bible():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://66.55.145.43:8018/listen.pls"])
    return "OK"

@app.route('/biblia/', methods=['POST'])
def play_bibla():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://94.23.6.53:8358/listen.pls"])
    return "OK"

@app.route('/birds/', methods=['POST'])
def play_birds():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://209.126.119.76:8200/listen.pls"])
    return "OK"

@app.route('/ocean/', methods=['POST'])
def play_ocean():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://5.39.71.159:8157/listen.pls"])
    return "OK"

@app.route('/100/', methods=['POST'])
def vol_100():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "100%"])
    return "OK"

@app.route('/75/', methods=['POST'])
def vol_75():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "75%"])
    return "OK"

@app.route('/50/', methods=['POST'])
def vol_50():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "50%"])
    return "OK"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
