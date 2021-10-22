#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import board
import busio
import adafruit_pca9685

i2c = busio.I2C(board.SCL,board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 1000
left_outer = pca.channels[1]
left_inner = pca.channels[2]

turning = False

def callback(data):
    rospy.loginfo(data.data)
    if turning:
        left_outer.duty_cycle = data.data
        left_inner.duty_cycle = data.data * .712
    else:
        left_outer.duty_cycle = data.data
        left_inner.duty_cycle = data.data
    
def rightCallback(rightData):
    rospy.loginfo(rightData.data)

def left_wheels():
    rospy.init_node('left_wheels')
    rospy.Subscriber('left_wheels', Int32, callback)
    rospy.Subscriber('right_wheels', Int32, rightCallback)
    rospy.spin()

if __name__ == '__main__':
    left_wheels()
