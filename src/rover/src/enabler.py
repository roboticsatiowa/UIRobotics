#!/usr/bin/env python3

import time
import rospy
from std_msgs.msg import  Bool
import RPi.GPIO as GPIO

output_pin = 18 # 12 on Jetson Nano header

GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

def listener():

    rospy.init_node('enabler')
    rospy.Subscriber('/enabled', Bool, enabled_callback)
    rospy.spin()
    
    rospy.loginfo("Cleaning GPIO pins...")
    GPIO.cleanup()

def enabled_callback(data):
    if data.data:
        GPIO.output(output_pin, GPIO.LOW)
    else:
        GPIO.output(output_pin, GPIO.HIGH)

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
