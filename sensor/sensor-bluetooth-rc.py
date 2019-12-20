#!/usr/bin/python

import bluetooth

result = bluetooth.lookup_name('DC:0C:5C:A1:14:6B', timeout=5)
if (result != None):
    exit(200)
else:
    exit(404)

