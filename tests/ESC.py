#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
# #fileOverview 电调控制程序 
#
#
#

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)

p = GPIO.PWM(7, 50)  # 通道为 12 频率为 50Hz

p.start(5)
time.sleep(2)
p.ChangeDutyCycle(6.05)

try:
    time.sleep(1000)

except KeyboardInterrupt:

    p.stop()
    GPIO.cleanup()
