#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL,board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 1000
pwm_channel = pca.channels[1]

def callback(data):
    rospy.loginfo(data.data)
    pwm_channel.duty_cycle = data.data

def pwm_driver():
    rospy.init_node('pwm_driver')
    rospy.Subscriber('pwm_signal',Int32,callback)
    rospy.spin()

if __name__ == '__main__':
    pwm_driver()
