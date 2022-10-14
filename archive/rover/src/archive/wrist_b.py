#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import board
import busio
import adafruit_pca9685

i2c = busio.I2C(board.SCL,board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 1000
w_channel = pca.channels[3]

def callback_b(data):
    w_channel.duty_cycle = data.data
    rospy.loginfo(data.data)

def wrist_b():
    rospy.init_node('wrist_b')
    rospy.Subscriber('wrist_b',Int32,callback_b)
    rospy.spin()

if __name__ == '__main__':
    wrist_b()
