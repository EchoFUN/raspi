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

GPIO.output(38, False)
GPIO.output(40, False)

p = GPIO.PWM(40, 200)  # 通道为 12 频率为 50Hz

p.start(20)


time.sleep(5)

p.ChangeDutyCycle(80)

time.sleep(5)

p.ChangeDutyCycle(100)
try:
    time.sleep(1000)

except KeyboardInterrupt:

    p.stop()
    GPIO.cleanup()

    pass
