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
#
#

from conf import PORTS


def run(GPIO, signal):

    GPIO.setmode(GPIO.BOARD)

    CarLeft = PORTS['CarLeft']
    CarRight = PORTS['CarRight']
    GPIO.setup(CarLeft + CarRight, GPIO.OUT)

    GPIO.output(CarLeft + CarRight, (True, False, True, False))
