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

pi = pigpio.pi('127.0.0.1', '8888')
if not pi.connected:
    exit(0)

print('connected to the pi ')

pi.set_servo_pulsewidth(12, 1200)
time.sleep(3)
pi.set_servo_pulsewidth(12, 1250)
time.sleep(3)
pi.set_servo_pulsewidth(12, 1300)
time.sleep(3)
pi.set_servo_pulsewidth(12, 1350)
time.sleep(3)
pi.set_servo_pulsewidth(12, 1200)

try:

    time.sleep(1000)
except KeyboardInterrupt:

    pi.set_servo_pulsewidth(12, 1000)
    pi.stop()
