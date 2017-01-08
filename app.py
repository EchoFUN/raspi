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

from conf import SERVER

try:
    import RPi.GPIO as GPIO
    import atexit

    atexit.register(GPIO.cleanup)
except ImportError:
    print('Not the Pi env !')

import directives
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

import os, socketIO_client
from socketIO_client import SocketIO, LoggingNamespace


def receiveDirectives(args):
    directive = args['D']
    if args.has_key('S'):
        signal = args['S']
    else:
        signal = ''

    global GPIO # Fuck the Global vars cost me severl hours ! :()
    try: 
        GPIO
    except NameError:
        GPIO = {}

    try:
        getattr(__import__('directives.' + directive), directive).run(GPIO, signal)
    except ImportError:
        print('Directive not found on the CAR ！')

if __name__ == "__main__" :

    socketIO = SocketIO(SERVER['ip'], SERVER['port'], LoggingNamespace, params={'specify': 'CAR'})

    socketIO.on('directives', receiveDirectives)
    socketIO.wait()