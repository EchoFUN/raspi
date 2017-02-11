#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
# #fileOverview 树莓派自带 RPi.GPIO 库 PWM 信号不准确
#
#
#

# PWM控制信号周期20ms, 脉宽 0.5ms-2.5ms 对应的角度-90到+90度, 范围180度(3度左右偏差), 当脉宽1.5ms时舵机在中立点(0度);

import time
import pigpio

# PIN_CODDE = 12
PIN_CODDE = 4

pi = pigpio.pi()
if not pi.connected:
    exit(0)

# pi.set_servo_pulsewidth(PIN_CODDE, 1400)
pi.set_servo_pulsewidth(PIN_CODDE, 1100)

pi.stop()
