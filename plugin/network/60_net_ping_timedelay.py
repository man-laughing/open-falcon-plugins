#!/usr/bin/env python

import os
import time
import json

hostt=os.getenv('HOSTNAME')
timee=int(time.time())
dns_reso  = '/usr/bin/dig ctc.flmp.parent.com &> /dev/null'

if os.system(dns_reso) == 0:
    ll = []
    command = "ping -c 10 ctc.flmp.parent.com -A |grep 'time='|awk -F'=' '{print $4}'|awk '{print $1}'"
    abc = os.popen(command).readlines()
    for i in abc:
        ll.append(int(float(i)))
    sum = 0 
    for ii in ll:
        sum = sum + ii
    value = sum / 10
    aaa = [ {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.timedelay','value':value,'counterType':'GAUGE','step':60} ]
    bbb = json.dumps(aaa)
    print bbb
