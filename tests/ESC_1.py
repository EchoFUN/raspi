#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
# #fileOverview 使用 pigpio hardware PWM . 来解决精度不准的问题
#
#
#


import time
import pigpio

PIN_CODDE = 4

pi = pigpio.pi()
if not pi.connected:
    exit(0)

# 第二个参数指代了PWM信号脉宽，1000us的脉宽表示了0%的油门，2000us的脉宽表示了100%的油门。
# 1150 指代了约 （1150 - 1000）/ 1000 * 100% = 15% 的油门。
pi.set_servo_pulsewidth(PIN_CODDE, 1220)

try:

    time.sleep(1000)
except KeyboardInterrupt:
    pi.set_servo_pulsewidth(PIN_CODDE, 0)
    pi.stop()
