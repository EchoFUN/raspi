#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
#
#
#

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(38, gpio.OUT)
gpio.setup(40, gpio.OUT)

gpio.output(38, False)
gpio.output(40, False)

switch = True
counter = 0

try:
    while True:

        switch = not switch
        gpio.output(40, switch)

        time.sleep(1)

        counter = counter + 1

        if counter == 200:
            break

except KeyboardInterrupt:
    pass

finally:
    gpio.cleanup()
