import nest
import time
import tweepy
import redis
#
# Redis
#
redb = redis.StrictRedis(host='localhost', port=6379, db=0)

client_id = redb.get('nest_client_id')
client_secret = redb.get('nest_client_secret')
access_token_cache_file = 'nest.json'


#
# Nest
#
napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)

if napi.authorization_required:
    #print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
    #if sys.version_info[0] < 3:
    #    pin = raw_input("PIN: ")
    #else:
    #    pin = input("PIN: ")
    pin = redb.get('nest_pin')
    napi.request_token(pin)

ts = time.time()
nest_status = "{}\n".format(ts)
# Access advanced structure properties:
for structure in napi.structures:
# Access advanced device properties:
    for device in structure.thermostats:
        nest_status += ('Device: %s\n' % device.name)
        nest_status += ('Where: %s\n' % device.where)
        nest_status += ('Mode       : %s\n' % device.mode)
        nest_status += ('HVAC State : %s\n' % device.hvac_state)
        nest_status += ('Fan        : %s\n' % device.fan)
        nest_status += ('Fan Timer  : %i\n' % device.fan_timer)
        nest_status += ('Temp       : %0.1fC\n' % device.temperature)
        nest_status += ('Humidity   : %0.1f%%\n' % device.humidity)
        nest_status += ('Target     : %0.1fC\n' % device.target)
        nest_status += ('Eco High   : %0.1fC\n' % device.eco_temperature.high)
        nest_status += ('Eco Low    : %0.1fC\n' % device.eco_temperature.low)
        nest_status += ('hvac_emer_heat_state  : %s\n' % device.is_using_emergency_heat)
        nest_status += ('online                : %s\n' % device.online)

#redb.set('nest_status',nest_status)
#
#
# Tweet
#
consumer_key = redb.get('twitter_consumer_key')
consumer_secret = redb.get('twitter_consumer_secret')
access_token = redb.get('twitter_access_token')
access_token_secret = redb.get('twitter_access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
tapi = tweepy.API(auth)
tapi.update_status(nest_status)
