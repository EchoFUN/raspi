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



GPIO.wait_for_edge(7, GPIO.FALLING)

try:
    while True:
        if GPIO.input(7) == GPIO.HIGH:
            print('Yes, high .')
        else:
            print('Not, high .')
        
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

finally:
    print('\nstop the pwm .')
    p.stop()
    GPIO.cleanup()
