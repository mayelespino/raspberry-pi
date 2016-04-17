from iron_cache import *

cache = IronCache()
try:
    item = cache.get(cache="test_cache", key="mykey")
except:
    item = None    
print item.value if item else print None
