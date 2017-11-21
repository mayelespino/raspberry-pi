#
#
import bluetooth
import requests
import redis

target_name = 'iPhone'
target_address = 'DC:0C:5C:A1:14:6B'

if bluetooth.lookup_name(target_address) == target_name:
    target_found = True
else:
    target_found = False

r = redis.StrictRedis(host='localhost', port=6379, db=0)
lock = r.get('chaperon_lock')

if target_found is True and lock != 'true':
    requests.post('http://picron.local:5000/say/hello_and_welcome_home_Maayyell/')
    r.set('chaperon_lock','true')
elif target_found is not True and lock == 'true':
    requests.post('http://picron.local:5000/say/come_back_soon_Maayyell/')
    r.set('chaperon_lock','false')


