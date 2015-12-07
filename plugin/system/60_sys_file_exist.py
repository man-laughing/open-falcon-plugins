#!/usr/bin/env python

import os
import json
import time


dir_path = '/var/www/html/corefile'
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

aa = os.listdir(dir_path)
if len(aa) == 0:
    value = 0
else:
    value = len(aa)

hostt=os.getenv('HOSTNAME')
timee=int(time.time())
aaa = [ {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'sys_file.exists','value':value,'counterType':'GAUGE','step':60} ]
bbb = json.dumps(aaa)
print bbb
