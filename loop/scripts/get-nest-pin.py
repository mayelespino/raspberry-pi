import nest
import sys
import redis

redb = redis.StrictRedis(host='localhost', port=6379, db=0)

client_id = redb.get('nest_client_id')
client_secret = redb.get('nest_client_secret')
access_token_cache_file = 'nest.json'

napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)

if napi.authorization_required:
    print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
    if sys.version_info[0] < 3:
        pin = raw_input("PIN: ")
    else:
        pin = input("PIN: ")
    napi.request_token(pin)

for structure in napi.structures:
    print ('Structure %s' % structure.name)
    print ('    Away: %s' % structure.away)
    print ('    Devices:')
    for device in structure.thermostats:
        print ('        Device: %s' % device.name)
        print ('            Temp: %0.1f' % device.temperature)

# Access advanced structure properties:
for structure in napi.structures:
    print ('Structure   : %s' % structure.name)
    print (' Postal Code                    : %s' % structure.postal_code)
    print (' Country                        : %s' % structure.country_code)
    print (' num_thermostats                : %s' % structure.num_thermostats)

# Access advanced device properties:
    for device in structure.thermostats:
        print ('        Device: %s' % device.name)
        print ('        Where: %s' % device.where)
        print ('            Mode       : %s' % device.mode)
        print ('            HVAC State : %s' % device.hvac_state)
        print ('            Fan        : %s' % device.fan)
        print ('            Fan Timer  : %i' % device.fan_timer)
        print ('            Temp       : %0.1fC' % device.temperature)
        print ('            Humidity   : %0.1f%%' % device.humidity)
        print ('            Target     : %0.1fC' % device.target)
        print ('            Eco High   : %0.1fC' % device.eco_temperature.high)
        print ('            Eco Low    : %0.1fC' % device.eco_temperature.low)

        print ('            hvac_emer_heat_state  : %s' % device.is_using_emergency_heat)

        print ('            online                : %s' % device.online)
