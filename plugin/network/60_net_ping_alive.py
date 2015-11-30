#!/usr/bin/env python

import os
import time
import json

hostt=os.getenv('HOSTNAME')
timee=int(time.time())
dns_reso  = '/usr/bin/dig ctc.flmp.parent.com &> /dev/null'

if os.system(dns_reso) == 0:
    ping_comm = 'ping -c 10  ctc.flmp.parent.com  -A &> /dev/null'
    if os.system(ping_comm) == 0:
        alive_value = 1
    else:
        alive_value = 0
    aaa = [ {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.alive','value':alive_value,'counterType':'GAUGE','step':60} ]
    bbb = json.dumps(aaa)
    print bbb




