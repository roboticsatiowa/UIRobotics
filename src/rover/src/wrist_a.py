#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import board
import busio
import adafruit_pca9685

i2c = busio.I2C(board.SCL,board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 1000
w_channel = pca.channels[0]

def callback_a(data):
    w_channel.duty_cycle - data.data

def wrist_a():
    rospy.init_node('wrist_a')
    rospy.Subscriber('wrist_a',Int32,callback_a)
    rospy.spin()

if __name__ == '__main__':
    wrist_a()
