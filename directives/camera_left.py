#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
#
#
#
#
#

from conf import DEGREE, PORTS
import time

reaTime = 0


def run(GPIO, signal):
    global reaTime
    reaTime = time.time()


def notify(GPIO, curTime):
    if not reaTime:
        pass
    else:
        action(GPIO, int((curTime - reaTime) / 0.02))


def caledCycle():
    return 2.5 + DEGREE['horizontal'] / 180


def action(GPIO, counter):
    GPIO.setmode(GPIO.BOARD)
    port = PORTS['CameraHorizontal']
    GPIO.setup(port, GPIO.OUT)

    p = GPIO.PWM(port, 50)  # 50HZ
    try: 
        global DEGREE
        DEGREE['horizontal'] += counter * 10

        p.start(caledCycle())
    except ValueError:
        pass
    time.sleep(0.5)

    p.stop()
    global reaTime
    reaTime = 0