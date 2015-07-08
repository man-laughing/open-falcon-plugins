#!/usr/bin/python
from __future__ import division
import os
import time
import json

r=open('/sys/class/net/eth1/statistics/rx_bytes','r')
r_int=int(r.read())
time.sleep(1)
rr=open('/sys/class/net/eth1/statistics/rx_bytes','r')
rr_int=int(rr.read())
input_flux =  (rr_int - r_int)  * 8 / 1024 / 1024

hostt=os.getenv('HOSTNAME')
timee=int(time.time())
aaa = [ {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.flux_input.eth1','value':input_flux,'counterType':'GAUGE','step':60} ]
bbb = json.dumps(aaa)
print bbb
