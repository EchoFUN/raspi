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



GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


GPIO.output(12, True)
GPIO.output(13, False)
GPIO.output(15, False)
GPIO.output(16, True)


time.sleep(0.25)
GPIO.cleanup()

