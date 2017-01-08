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

import camera_down
import camera_up
import camera_left
import camera_right

import time


def run(GPIO, signal):

    curTime = time.time()

    camera_down.notify(GPIO, curTime)
    camera_up.notify(GPIO, curTime)
    camera_left.notify(GPIO, curTime)
    camera_right.notify(GPIO, curTime)