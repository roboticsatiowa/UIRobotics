#!/usr/bin/env python3

import time
import rospy
from std_msgs.msg import  Bool
import RPi.GPIO as GPIO

class Enabler():
    def __init__(self):
        self.output_pin = 18 # 12 on Jetson Nano header

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.HIGH)

        # ros pub and sub
        rospy.Subscriber('/enabled', Bool, self.enabled_callback)

    def listen(self):
        rospy.spin()

        # cleanup on aisle GPIO
        rospy.loginfo("Cleaning GPIO pins...")
        GPIO.cleanup()

    def enabled_callback(self, data):
        if data.data:
            GPIO.output(output_pin, GPIO.LOW)
        else:
            GPIO.output(output_pin, GPIO.HIGH)


if __name__ == '__main__':
    try:
        # initialize ros node
        rospy.init_node('enabler')

        enabler = Enabler()
        enabler.listen()
    except rospy.ROSInterruptException:
        pass
