#!/usr/bin/env python

import threading
import Queue
import os
import time
import json

result = []
iplist = '/usr/local/falcon-agent/plugin/plugin/network/iplist_test'
hostt = os.getenv('HOSTNAME')
timee = int(time.time())

_thread = 10
run1_ctc_queue = Queue.Queue()
run1_cnc_queue = Queue.Queue()
run2_ctc_queue = Queue.Queue()
run2_cnc_queue = Queue.Queue()
run3_ctc_queue = Queue.Queue()
run3_cnc_queue = Queue.Queue()

#Add the ctc and cnc ip queue.
with open(iplist,'r') as f:
    ff = f.readlines()
for ip in ff:
    ipp = ip.replace('\n','').split()
    if ipp[0] == 'ctc':
        run1_ctc_queue.put(ipp[1]+'-'+ipp[2])
        run2_ctc_queue.put(ipp[1]+'-'+ipp[2])
        run3_ctc_queue.put(ipp[1]+'-'+ipp[2])
    elif ipp[0] == 'cnc':
        run1_cnc_queue.put(ipp[1]+'-'+ipp[2])
        run2_cnc_queue.put(ipp[1]+'-'+ipp[2])
        run3_cnc_queue.put(ipp[1]+'-'+ipp[2])

def ping_alive(q):
    while True:
        sumstr  = q.get() 
        desc    = sumstr.split('-')[0]
        ipaddr  = sumstr.split('-')[1]
        if os.system("ping -c 1  %s &> /dev/null" %ipaddr) == 0:
            alive_value = 1 
        else:
            alive_value = 0
        aaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.alive.'+desc+'.'+ipaddr.split('.')[-2]+'.'+ipaddr.split('.')[-1],'value':alive_value,'counterType':'GAUGE','step':300}
        result.append(aaa)
        if hostt.split('-')[1] == 'ctc':
            run1_ctc_queue.task_done() 
        else:
            run1_cnc_queue.task_done() 

def ping_losepack(q):
    while True:
        total = q.get() 
        aa    = total.split('-')[0]
        bb    = total.split('-')[1]
        losepack_comm = "ping -c 100 -A "+ bb +"|grep pack |awk '{print $6}'|sed 's/\%//g'"
        losepack_value = os.popen(losepack_comm).read()
        int_losepack_value = int(losepack_value)
        aaaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.losepack.'+aa+'.'+bb.split('.')[-2]+'.'+bb.split('.')[-1],'value':int_losepack_value,'counterType':'GAUGE','step':300}
        result.append(aaaa)
        if hostt.split('-')[1] == 'ctc':
            run2_ctc_queue.task_done() 
        else:
            run2_cnc_queue.task_done() 

def ping_timedelay(q):
    while True:
        zz = q.get() 
        zzz   = zz.split('-')[0]
        zzzz  = zz.split('-')[1]
        ll = []
        common = "ping -c 10 -A "+zzzz+"|grep 'time='|awk -F'=' '{print $4}'|awk '{print $1}'"
        abc = os.popen(common).readlines()
        for z in abc:
            ll.append(int(float(z)))
        sum = 0 
        for iii in ll:
            sum = sum + iii
            ping_timedelay_value = sum / 10

        aaaaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.timedelay.'+zzz+'.'+zzzz.split('.')[-2]+'.'+zzzz.split('.')[-1],'value':ping_timedelay_value,'counterType':'GAUGE','step':300}
        result.append(aaaaa)
        if hostt.split('-')[1] == 'ctc':
            run3_ctc_queue.task_done() 
        else:
            run3_cnc_queue.task_done() 

for i in range(_thread):
    if hostt.split('-')[1] == 'ctc':
        run1 = threading.Thread(target=ping_alive,args=(run1_ctc_queue,))
        run2 = threading.Thread(target=ping_losepack,args=(run2_ctc_queue,))
        run3 = threading.Thread(target=ping_timedelay,args=(run3_ctc_queue,))
        run1.setDaemon(True)
        run2.setDaemon(True)
        run3.setDaemon(True)
        run1.start()   
        run2.start()   
        run3.start()   
    elif hostt.split('-')[1] == 'cnc':
        run1 = threading.Thread(target=ping_alive,args=(run1_cnc_queue,))
        run2 = threading.Thread(target=ping_losepack,args=(run2_cnc_queue,))
        run3 = threading.Thread(target=ping_timedelay,args=(run3_cnc_queue,))
        run1.setDaemon(True)
        run2.setDaemon(True)
        run3.setDaemon(True)
        run1.start()   
        run2.start()   
        run3.start()   
run1_ctc_queue.join()
run1_cnc_queue.join()
run2_ctc_queue.join()
run2_cnc_queue.join()
run3_ctc_queue.join()
run3_cnc_queue.join()

bbb = json.dumps(result)
print bbb
