#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
# #fileOverview 小车模拟运行测试代码
#
#
#

import RPi.GPIO as GPIO
import time

import atexit

atexit.register(GPIO.cleanup)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


GPIO.output(12, False)
GPIO.output(13, True)
GPIO.output(15, True)
GPIO.output(16, False)


time.sleep(20000)
