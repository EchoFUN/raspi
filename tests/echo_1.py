#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
# @fileOverview 回环程序检测，可以根据声波传输和接受的速度，用来测试距离之用。
#
#
#
#

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(7, GPIO.IN)

p = GPIO.PWM(11, 1000)  # 100HZ 脉冲周期为 1000 / 1000 = 1 ms
p.start(5)  # 高电平的频宽为 1000 / 0.05 = 50 us 

# wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
channel = GPIO.wait_for_edge(7, GPIO.FALLING, timeout=5000)
last = time.time()
if channel is None:
    print('Timeout occurred')
else:

    current = time.time()
    print(last - current)
    print('Edge detected on channel', channel)

p.stop()
GPIO.cleanup()
