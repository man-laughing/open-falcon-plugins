#!/usr/bin/env  python
#Author:  Laughing
#MAIL:    305835227@qq.com

import time
import os
import json

hostt=os.getenv('HOSTNAME')
timee=int(time.time())
value = os.path.getsize('/usr/sbin/lsof')
if value == 145872:
    size_value = 1
else:
    size_value = 0
aaa = [ {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'sys.size.lsof','value':size_value,'counterType':'GAUGE','step':60} ]
bbb = json.dumps(aaa)
print bbb


