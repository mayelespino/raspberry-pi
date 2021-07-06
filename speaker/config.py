class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    STATIONS = { 
              "nature1" : "http://192.240.102.198:14244/listen.pls",
              "nature2" : "http://5.39.71.159:8157/listen.pls",
              "nature3" : "http://162.244.80.118:9196/listen.pls",
              "chill1" : "http://192.99.17.12:4516/listen.pls",
              "chill2" : "http://192.99.17.12:4950/listen.pls",
              "trance1" : "http://uk4.internet-radio.com:8049/listen.pls",
              "trance2" : "http://hirschmilch.de:7000/listen.pls",
              "bass1" : "http://uk1.internet-radio.com:8118/listen.pls",
              "experimental1" : "http://dallas.myautodj.com:8099/listen.pls",
              "experimental2" : "http://akademieradio.de:80/play.m3u",
              "experimental3" : "http://198.27.66.225:8570/listen.pls",
              "experimental4" : "http://198.15.77.50:9368/listen.pls",
              "experimental5" : "http://50.7.68.251:6982/listen.pls",
              "dogs1" : "http://99.198.118.250:8241/listen.pls",
              "dogs2" : "http://yp.shoutcast.com/sbin/tunein-station.pls?id=1794904",
              "dogs3" : "http://yp.shoutcast.com/sbin/tunein-station.pls?id=1632399",
              "talk1" : "http://176.31.98.109:4962/listen.pls",
              "talk2" : "http://69.46.24.226:7006/listen.pls",
              "talk3" : "http://74.50.122.103:7372/listen.pls",
              "talk4" : "http://95.211.3.65:9185/listen.pls",
              "bible" : "http://64.71.79.181:6552/listen.pls"
              }
