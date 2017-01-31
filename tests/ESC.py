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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50) # 50Hz，每个信号周期为 1000 / 50 = 20ms； dutyCycle为5，则为1ms(1000us)最低油门；10为2ms(2000us)最高油门
p.start(5)
time.sleep(2)

p.ChangeDutyCycle(5.5) # 油门大约在 10%的样子

raw_input('Press return to stop !')
p.stop()
GPIO.cleanup()