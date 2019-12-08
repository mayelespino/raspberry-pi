from flask import Flask
import subprocess 

app = Flask(__name__)

#
# Health check
#

@app.route('/')
def hello_world():
    return 'OK'

#
# Internet Radio
#

@app.route('/mute/', methods=['POST'])
def play_mute():
    subprocess.Popen(["/usr/bin/pkill","mplayer","-c"])
    return "play_mute - OK"

@app.route('/scanner/', methods=['POST'])
def play_scanner():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://198.178.123.20:10488/listen.pls"])
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://104.167.4.67:8296/listen.pls"])
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://162.244.80.118:9196/listen.pls"])
    return "play_scanner - OK"

@app.route('/nature/', methods=['POST'])
def play_nature():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://94.23.252.14:8067/listen.pls"])
    return "play_nature - OK"

@app.route('/pink/', methods=['POST'])
def play_pink():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://uk1.internet-radio.com:8004/listen.pls"])
    return "play_pink - OK"

@app.route('/bible/', methods=['POST'])
def play_bible():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://66.55.145.43:8018/listen.pls"])
    return "play_bible - OK"

@app.route('/biblia/', methods=['POST'])
def play_bibla():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://94.23.6.53:8358/listen.pls"])
    return "play_biblia - OK"

@app.route('/birds/', methods=['POST'])
def play_birds():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://209.126.119.76:8200/listen.pls"])
    return "play_birds - OK"

@app.route('/ocean/', methods=['POST'])
def play_ocean():
    subprocess.Popen(["/usr/bin/mplayer","-playlist","http://5.39.71.159:8157/listen.pls"])
    return "play_ocean - OK"

#
# Volume
#

@app.route('/100/', methods=['POST'])
def vol_100():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "100%"])
    return "vol_100 - OK"

@app.route('/95/', methods=['POST'])
def vol_95():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "95%"])
    return "vol_95 - OK"

@app.route('/85/', methods=['POST'])
def vol_85():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "85%"])
    return "vol_85 - OK"

@app.route('/75/', methods=['POST'])
def vol_75():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "75%"])
    return "vol_75 - OK"

@app.route('/50/', methods=['POST'])
def vol_50():
    subprocess.Popen(["sudo","/usr/bin/amixer","set", "PCM", "--", "50%"])
    return "vol_50 -OK"

#
# SIRI
#

@app.route('/siri_news/', methods=['POST'])
def siri_news():
    subprocess.Popen(["/usr/bin/mplayer","/media/mp3/text2speach/siri_news.mp3"])
    return "siri_news -  OK"

@app.route('/siri_stop/', methods=['POST'])
def siri_stop():
    subprocess.Popen(["/usr/bin/mplayer","/media/mp3/text2speach/siri_stop.mp3"])
    return "siri_stop -  OK"

@app.route('/siri_waitwait/', methods=['POST'])
def siri_waitwait():
    subprocess.Popen(["/usr/bin/mplayer","/media/mp3/text2speach/siri_play_waitwait.mp3"])
    return "siri_waitwait -  OK"

#
# Text to speach
#
@app.route('/whoisit/', methods=['POST'])
def say_whoisit():
    subprocess.Popen(["/usr/bin/mplayer","/media/mp3/text2speach/who_is_it.mp3"])
    return "say_whoisit -  OK"

@app.route('/quienes/', methods=['POST'])
def say_quienes():
    subprocess.Popen(["/usr/bin/mplayer","/media/mp3/text2speach/quien_es.mp3"])
    return "say_quienes -  OK"

#
# Utils
#
@app.route('/cron/', methods=['POST'])
def util_cron():
    p = subprocess.Popen(["/usr/bin/crontab","-l"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out

@app.route('/date_time/', methods=['POST'])
def util_date_time():
    p = subprocess.Popen(["/bin/date"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out

#
# MAIN
#
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
