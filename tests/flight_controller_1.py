#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
# 
# @fileOverview APM 飞行控制器校准程序控制
#
#
#

import time
import pigpio
import os
import readchar

from excepts import *

throttle = 1000
STEP = 100


def readerEvent():
    global throttle
    while True:
        code = repr(readchar.readkey())
        token = code[-2]

        if len(code) == 3:

            if token == 'w':
                throttle -= STEP

            elif token == 's':
                throttle += STEP

            pi.set_servo_pulsewidth(12, throttle)


def connectPi(url, port):
    pi = pigpio.pi(url, port)
    if not pi.connected:
        raise PiConnectError

    return pi


def unlockQuad(pi):
    pass


if __name__ == '__main__':

    global pi

    try:

        # Init the connection to the pigpio GPIO lib.
        os.system('clear')
        print('connected to the pi ... ')
        pi = connectPi('127.0.0.1', '8888')
        print('connected !')

        # Unlock the quad first.
        print('unlock the quad ...')
        unlockQuad(pi)
        print('unlocked !')

        # Enter the event loop, listening to the key evets.
        readerEvent()

    except KeyboardInterrupt:

        pi.set_servo_pulsewidth(12, 1000)
        pi.stop()
