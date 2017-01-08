#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
# 
# @fileOverview 使用 PWM 信号调试红色的发光二极管
#
#
#

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

GPIO.output(38, True)
GPIO.output(40, True)

p = GPIO.PWM(40, 200)  # 通道为 12 频率为 50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)

except KeyboardInterrupt:
    pass

p.stop()

GPIO.cleanup()
