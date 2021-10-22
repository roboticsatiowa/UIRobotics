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

mostRecentLeftData = -1
mostRecentRightData = -1

def callback(data):
    rospy.loginfo(data.data)
    mostRecentLeftData = data.data
    
    if mostRecentLeftData != -1 and mostRecentRightData != -1: # if these have been initialized
        # if either is less than 2^15 while the other is greater than 2^15, turning is True
        turning = (mostRecentLeftData - 32768 > 0 and mostRecentRightData - 32768 < 0) or (mostRecentLeftData - 32768 < 0 and mostRecentRightData - 32768 > 0)
    
    if turning:
        left_outer.duty_cycle = data.data
        left_inner.duty_cycle = data.data * .712
    else:
        left_outer.duty_cycle = data.data
        left_inner.duty_cycle = data.data
    
def rightCallback(rightData):
    rospy.loginfo(rightData.data)
    mostRecentRightData = rightData.data
    
    if mostRecentLeftData != -1 and mostRecentRightData != -1: # if these have been initialized
        # if either is less than 2^15 while the other is greater than 2^15, turning is True
        turning = (mostRecentLeftData - 32768 > 0 and mostRecentRightData - 32768 < 0) or (mostRecentLeftData - 32768 < 0 and mostRecentRightData - 32768 > 0)

def left_wheels():
    rospy.init_node('left_wheels')
    rospy.Subscriber('left_wheels', Int32, callback)
    rospy.Subscriber('right_wheels', Int32, rightCallback)
    rospy.spin()

if __name__ == '__main__':
    left_wheels()
