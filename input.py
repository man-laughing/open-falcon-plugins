#!/usr/bin/python
from __future__ import division
import os
import time

r=open('/sys/class/net/bond0/statistics/rx_bytes','r')
r_int=int(r.read())
time.sleep(1)
rr=open('/sys/class/net/bond0/statistics/rx_bytes','r')
rr_int=int(rr.read())
input_flux =  (rr_int - r_int)  * 8 / 1024 / 1024

input_flux_new=str("%.2f"%input_flux)
hostt=os.getenv('HOSTNAME')
timee=time.time()
aaa = [{'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.flux.eth0','value':input_flux_new,'counterType':'GAUGE','step':60}]
print aaa
