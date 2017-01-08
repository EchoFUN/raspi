#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
#
# {12, 13}, {15, 16}, {18, 22}
#

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(38, gpio.OUT)
gpio.setup(40, gpio.OUT)



gpio.output(38, True)
gpio.output(40, True)


switch = True
counter = 0
while True:

    switch = not switch
    gpio.output(40, switch)

    time.sleep(0.5)

    counter = counter + 1

    if counter == 50:
        break

gpio.cleanup()
