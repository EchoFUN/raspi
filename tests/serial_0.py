#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
# #fileOverview 树莓派串口操作事件，用来输入和输出陀螺仪数据信息 
#
#
#

from __future__ import division

import os
import sys
import math
import codecs

import serial

sensor = serial.Serial(port='/dev/ttyAMA0', baudrate='9600', timeout=1)


def convert(hexVal):
    return int(codecs.encode(hexVal, 'hex'), 16)


while True:
    data = sensor.read(size=1)
    if (data == b'\x55'):
        print('Get the data !')
        sensor.read(size=10)
        break

    print('trying', data)

try:
    while True:
        data = sensor.read(size=11)
        if not len(data) == 11:
            print('Byte error !')
            break

        if data[1] == b'\x50':

            # print(convert(data[7]))
            pass

        # Angle Output.
        if (data[1] == b'\x53'):
            hexVal = []
            for i in range(11):
                hexVal.append(convert(data[i]))

            ax = ((hexVal[3] << 8) | (hexVal[2] & 0xff)) / 32768 * 180
            ay = ((hexVal[5] << 8) | (hexVal[4] & 0xff)) / 32768 * 180
            az = ((hexVal[7] << 8) | (hexVal[6] & 0xff)) / 32768 * 180

            print(round(ax, 3), round(ay, 3), round(az, 3))

except KeyboardInterrupt:
    sensor.close()
    print('Close the sensor !')