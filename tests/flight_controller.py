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

pi = pigpio.pi()
if not pi.connected:
    exit(0)

SIMPLE_PIN = [21, 20, 16, 12, 26, 19, 13, 6]

for i in range(len(SIMPLE_PIN)):

    curr_pin = SIMPLE_PIN[i]

    if curr_pin == 16: 

        pi.set_servo_pulsewidth(curr_pin, 1500)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(curr_pin, 1000)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(curr_pin, 1250)
    else:

        pi.set_servo_pulsewidth(curr_pin, 1100)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(curr_pin, 1900)
        time.sleep(0.5)
        pi.set_servo_pulsewidth(curr_pin, 1500)


try:

    time.sleep(1000)
except KeyboardInterrupt:
    pi.stop()
