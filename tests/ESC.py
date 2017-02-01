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

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

p = GPIO.PWM(
    4, 400
)  # 400Hz，每个信号周期为 1000 / 400 = 2.5ms； dutyCycle为40，则为1ms(1000us)最低油门；80为2ms(2000us)最高油门
p.start(40)
time.sleep(2)

p.ChangeDutyCycle(45)  # 油门大约在 10%的样子

raw_input('Press return to stop !')
p.stop()
GPIO.cleanup()