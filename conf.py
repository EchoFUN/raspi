#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2016-12-04 星期日
#
#
# @fileOverview 引脚端口的配置文件
#
#
#


PORTS = {

  'CarLeft': [12, 13],

  'CarRight': [15, 16],

  'CameraVertical': 7,

  'CameraHorizontal': 32

}

# Camera init degree as global vars.
DEGREE = {
  'vertical': 0,

  'horizontal' : 0
}

# Server side address
SERVER = {
  'ip': '192.168.10.102',

  'port': '8080'
}
