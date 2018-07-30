import socket
from time import sleep
import threading
from queue import Queue
#definate the command
com_origin=b'\xff\x08\x00\x3f\x40\x3f\x10\x10\x10\x00\x09'#original state

com_hover=b'\xff\x08\x7e\x3f\x40\x3f\x90\x10\x10\x00\x0b'#hover state(without doing anything)

com_trigger=b'\xff\x08\x7e\x3f\x40\x3f\x90\x10\x10\x40\xcb'#youmen
com_speedup=b'\xff\x08\xfc\x3f\x40\x3f\x90\x10\x10\x40\x4d'#speed up

com_stop=b'\xff\x08\x7e\x3f\x40\x3f\x90\x10\x10\xa0\x6b'#stop ,i ma

com_turnleft=b'\xff\x08\x82\x00\x40\x3f\x90\x10\x10\x00\x46'
com_turnright=b'\xff\x08\x7e\x7e\x40\x3f\x90\x10\x10\x00\xcc'

com_moveahead=b'\xff\x08\x00\x3f\x01\x40\x90\x10\x10\x00\xc7'
com_moveback= b'\xff\x08\x00\x3f\x40\x7e\x90\x10\x10\x00\x4a'
com_moveleft= b'\xff\x08\x00\x3f\x7f\x3f\x90\x10\x10\x00\x4a'
com_moveright=b'\xff\x08\x00\x3f\x40\x00\x90\x10\x10\x00\xc8'

com_speeddown=b'\xff\x08\x5c\x3f\x40\x3f\x90\x10\x10\x00\x2d'#may not use


def outstream():
    while(True):
        a= input()
        if a=='w':
            a=com_speedup
        elif a=='s':
            a=com_speeddown
        elif a=='a':
            a=com_turnleft
        elif a=='d':
            a=com_turnright
        elif a=='j':
            a=com_moveleft
        elif a=='i':
            a=com_moveahead
        elif a=='l':
            a=com_moveright
        elif a=='k':
            a=com_moveback
        elif a=='r':
            a=com_hover
        elif a=='f':
            a=com_trigger
        elif a=='v':
            a=com_stop
        else:
            continue
        input_queue.put(a)

#set the target's address
IPADDR = '172.16.10.1'
PORTNUM = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# connect the socket
s.connect((IPADDR, PORTNUM))
inputthread=threading.Thread(target=outstream,daemon=True)
input_queue=Queue()
print('wsad as right stick and jkil as left stick\nyou can push r to hover and f to trig and push v to stop immediatly\n')
inputthread.start()
command=com_origin
# send a series of commands
while True:
    if not input_queue.empty():
        command=input_queue.get()
    s.send(command)
    sleep(0.05)

 

# close the socket
s.close()


def test():
    for n in range(0,20):
        s.send(com_origin)
        sleep(0.05)

    for n in range(0,20): 
        s.send(com_hover)
        sleep(0.05)

    for n in range(0,100): 
        s.send(com_trigger)
        sleep(0.05)

    for n in range(0,20): 
        s.send(com_speedup)
        sleep(0.05)

    for n in range(0,20): 
        s.send(com_turnleft)
        sleep(0.05)


    for n in range(0,100): 
        s.send(com_stop)
        sleep(0.05)