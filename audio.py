#!/usr/bin/env python3

import phatbeat
import signal
import os
from subprocess import call, Popen

proc = None
interrupted = False
playing = False

FNULL = open(os.devnull, 'w')

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)

@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def playpause(pin):
    global playing
    global proc
    if playing:
        print('stop playing')
        call(['kill', '-9', '%d' % proc.pid])
        proc.wait()
        playing = False
    else:
        print('start playing')
        proc = Popen(['mpg123', '--loop', '-1', '/home/pi/pi-sound-machine/waterfall.mp3'], shell=False, stdout=FNULL, stderr=FNULL)
        playing = True

@phatbeat.on(phatbeat.BTN_VOLUP)
def volume_up(pin):
    print('volume up')
    call(['amixer', 'set', 'Master', '10%+'], stdout=FNULL, stderr=FNULL)

@phatbeat.on(phatbeat.BTN_VOLDN)
def volume_down(pin):
    print('volume down')
    call(['amixer', 'set', 'Master', '10%-'], stdout=FNULL, stderr=FNULL)

if __name__ == "__main__":
    print("starting pirate radio script")
    while True:
        if interrupted:
            print("exiting pirate radio script")
            break

