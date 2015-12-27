#!/usr/bin/env python

import os
import time
import json

file_path = '/usr/local/falcon-agent/plugin/plugin/network/iplist'
result = []

def open_file():
    with open(file_path,'r') as f:
        ff = f.readlines()
    return ff


def ping_alive():
    hostt=os.getenv('HOSTNAME')
    timee=int(time.time())
    aa = open_file()
    for i in aa:
        ii = i.split()
        if hostt.split('-')[1] == 'ctc' or hostt.split('-')[1] == 'ck':
            ping_comm = 'ping -c 10 -A '+ii[1]+' &> /dev/null'
            if os.system(ping_comm) == 0:
                alive_value = 1
            else:
                alive_value = 0
            aaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.alive.'+ii[0]+'.'+ii[1].split('.')[-2]+'.'+ii[1].split('.')[-1],'value':alive_value,'counterType':'GAUGE','step':60}
            result.append(aaa)
        elif hostt.split('-')[1] == 'cnc' or hostt.split('-')[1] == 'yd':
            ping_comm = 'ping -c 10 -A '+ii[2]+' &> /dev/null'
            if os.system(ping_comm) == 0:
                alive_value = 1
            else:
                alive_avlue = 0
            aaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.alive.'+ii[0]+'.'+ii[2].split('.')[-2]+'.'+ii[2].split('.')[-1],'value':alive_value,'counterType':'GAUGE','step':60}
            result.append(aaa)
        else:
            pass

def ping_losepack():
    hostt=os.getenv('HOSTNAME')
    timee=int(time.time())
    bb = open_file()
    for i in bb:
        ii = i.split()
        if hostt.split('-')[1] == 'ctc' or hostt.split('-')[1] == 'ck':
            losepack_comm = "ping -c 10 -A "+ii[1]+"|grep pack |awk '{print $6}'|sed 's/\%//g'"
            value = os.popen(losepack_comm).read()
            int_value = int(value)
            aaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.losepack.'+ii[0]+'.'+ii[1].split('.')[-2]+'.'+ii[1].split('.')[-1],'value':int_value,'counterType':'GAUGE','step':60}
            result.append(aaa)
        elif hostt.split('-')[1] == 'cnc' or hostt.split('-')[1] == 'yd':
            losepack_comm = "ping -c 10 -A "+ii[2]+"|grep pack |awk '{print $6}'|sed 's/\%//g'"
            value = os.popen(losepack_comm).read()
            int_value = int(value)
            aaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.losepack.'+ii[0]+'.'+ii[2].split('.')[-2]+'.'+ii[2].split('.')[-1],'value':int_value,'counterType':'GAUGE','step':60}
            result.append(aaa)
        else:
            pass



def ping_timedelay():
    hostt=os.getenv('HOSTNAME')
    timee=int(time.time())
    bb = open_file()
    for i in bb:
        ii = i.split()
        if hostt.split('-')[1] == 'ctc' or hostt.split('-')[1] == 'ck':
            ll = []
            commor = "ping -c 10 -A "+ii[1]+"|grep 'time='|awk -F'=' '{print $4}'|awk '{print $1}'"
            abc = os.popen(commor).readlines()
            for z in abc:
                ll.append(int(float(z)))
            sum = 0 
            for iii in ll:
                sum = sum + iii
                value = sum / 10
            aaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.timedelay.'+ii[0]+'.'+ii[1].split('.')[-2]+'.'+ii[1].split('.')[-1],'value':value,'counterType':'GAUGE','step':60}
            result.append(aaa)
        elif hostt.split('-')[1] == 'cnc' or hostt.split('-')[1] == 'yd':
            ll = []
            commor = "ping -c 10 -A "+ii[2]+"|grep 'time='|awk -F'=' '{print $4}'|awk '{print $1}'"
            abc = os.popen(commor).readlines()
            for z in abc:
                ll.append(int(float(z)))
            sum = 0 
            for iii in ll:
                sum = sum + iii
                value = sum / 10
            aaa = {'endpoint':hostt,'tags':'','timestamp':timee,'metric':'net.ping.timedelay.'+ii[0]+'.'+ii[2].split('.')[-2]+'.'+ii[2].split('.')[-1],'value':value,'counterType':'GAUGE','step':60}
            result.append(aaa)
        else:
            pass

ping_alive()
ping_losepack()
ping_timedelay()
bbb = json.dumps(result)
print bbb
