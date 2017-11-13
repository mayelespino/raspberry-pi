#
# Credit due: I got the base for this script from:
# https://people.csail.mit.edu/albert/bluez-intro/c212.html
#
import bluetooth
import requests

target_name = "iPhone"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    requests.post('http://picron.local:5000/say/hello_and_welcome_home_Maayyell/')
else:
