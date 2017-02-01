#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2017-02-01 星期三 年初五
#
#
# #fileOverview 四轴飞行器手工起飞控制程序，手工调节四轴水平起飞。
#
#
#

import os
import time

from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))

    if key == keyboard.Key.esc:
        # Stop listener
        return False


def boot():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    boot()
