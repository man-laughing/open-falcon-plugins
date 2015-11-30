#!/usr/bin/env python

import os
import time
import json

hostt=os.getenv('HOSTNAME')
timee=int(time.time())
dns_reso  = '/usr/bin/dig ctc.flmp.parent.com &> /dev/null'
command = "ping -c 10 ctc.flmp.parent.com -A |grep pack |awk '{print $6}'|sed 's/\%//g'"
value = os.popen(command).read()
int_value = int(value)

if os.system(dns_reso) == 0:
    aaa = [ {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.losepack','value':int_value,'counterType':'GAUGE','step':60} ]
    bbb = json.dumps(aaa)
    print bbb

