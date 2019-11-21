import requests

x = requests.get('http://sensor.local')
print(x.status_code)
