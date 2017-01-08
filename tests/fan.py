#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
# @fileOverview PMW 进行风扇转速的控制。
#
#
#
#

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

GPIO.output(13, False)

time.sleep(5)
GPIO.cleanup()