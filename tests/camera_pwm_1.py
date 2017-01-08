#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
# #fileOverview PMW 调试测试
#
#
#

import RPi.GPIO as GPIO
import time
import atexit

atexit.register(GPIO.cleanup)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=False)

p = GPIO.PWM(7, 50)  #50HZ

p.start(1.5)

time.sleep(2)
p.ChangeDutyCycle(0)

p.stop()

# PWM控制信号周期20ms, 脉宽 0.5ms-2.5ms 对应的角度-90到+90度, 范围180度(3度左右偏差), 当脉宽1.5ms时舵机在中立点(0度);


# while (True):
#     for i in range(0, 181, 10):

#         cycle = 1.2 + 10 * i / 180
#         p.ChangeDutyCycle(cycle)  #设置转动角度  

#         print('高电平脉宽：' + bytes(cycle))
#         time.sleep(0.02)  #等该20ms周期结束  
#         p.ChangeDutyCycle(0)  #归零信号  



#     for i in range(181, 0, -10):

#         cycle = 1.2 + 10 * i / 180
#         p.ChangeDutyCycle(cycle)
#         print('高电平脉宽：' + bytes(cycle))
#         time.sleep(0.02)
#         p.ChangeDutyCycle(0)
