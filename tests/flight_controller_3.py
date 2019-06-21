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




try:

    time.sleep(2)

    print('Start The throtte.')
    pi.set_servo_pulsewidth(16, 1100)

    time.sleep(1000)
except KeyboardInterrupt:

    pi.set_servo_pulsewidth(16, 1000)
    pi.stop()
