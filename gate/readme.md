# gate - Interface with devices in the home and outside world
# Home APIs

# Links and Notes
- https://developers.nest.com/documentation/cloud/sample-code-auth
- https://pypi.python.org/pypi/python-nest
- https://stackoverflow.com/questions/19091087/open-redis-port-for-remote-connections
```
Did you set the bind option to allow remote access on the redis server?

Before (file /etc/redis/redis.conf)

bind 127.0.0.1
After

bind 0.0.0.0
```

- To solve the overcommit issue on the server
```
[1035] 22 Nov 00:34:31.443 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysc
```
