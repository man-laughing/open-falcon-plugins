#!/usr/bin/python

import time
import os
import hashlib
import json

with open('/bin/ps','r') as f:
    ff = f.read() 
m = hashlib.md5(ff)
m_str = m.hexdigest()
if m_str == '58cc183550b2c4b46c9cf53c6b387297':
    md5_value = 1
else:
    md5_value = 0
hostt=os.getenv('HOSTNAME')
timee=int(time.time())
aaa = [ {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'sys.md5.ps','value':md5_value,'counterType':'GAUGE','step':60} ]
bbb = json.dumps(aaa)
print bbb
