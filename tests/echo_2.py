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

from hcsr04sensor import sensor

GPIO.setmode(GPIO.BCM)

#set GPIO direction (IN / OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)


def distance():
    value = sensor.Measurement(17, 4)
    raw_measurement = value.raw_distance()

    # Calculate the distance in centimeters
    metric_distance = value.distance_metric(raw_measurement)

    print("The Distance = {} centimeters".format(metric_distance))


if __name__ == '__main__':
    try:
        while True:
            distance()
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
    except ValueError:
        GPIO.cleanup()
