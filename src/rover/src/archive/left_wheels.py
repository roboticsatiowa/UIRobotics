#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import board
import busio
import adafruit_pca9685

class LeftWheels():
    def __init__(self):
        i2c = busio.I2C(board.SCL,board.SDA)
        pca = adafruit_pca9685.PCA9685(i2c)
        pca.frequency = 1000
        self.left_outer = pca.channels[6]
        self.left_inner = pca.channels[9]

        self.mostRecentLeftData = -1
        self.mostRecentRightData = -1

        # ros pub and sub
        rospy.Subscriber('left_wheels', Int32, self.left_callback)
        rospy.Subscriber('right_wheels', Int32, self.right_callback)

    def run(self):
        rospy.spin()

    def left_callback(self, data):
        self.mostRecentLeftData = data.data
    
        turning = False
        if self.mostRecentLeftData != -1 and self.mostRecentRightData != -1: # if these have been initialized
            # if either is less than 2^15 while the other is greater than 2^15, turning is True
            turning = (self.mostRecentLeftData - 32768 > 0 and self.mostRecentRightData - 32768 < 0) or (self.mostRecentLeftData - 32768 < 0 and self.mostRecentRightData - 32768 > 0)
        
        if turning:
            self.left_outer.duty_cycle = int(data.data/(4/3))+8192
            self.left_inner.duty_cycle = int(data.data/(4/3))+8192
            #left_inner.duty_cycle = int((((data.data-32768)*.793)+32768)/(4/3))+8192
        else:
            self.left_outer.duty_cycle = int(data.data/(4/3))+8192
            self.left_inner.duty_cycle = int(data.data/(4/3))+8192

    def right_callback(self, data):
        self.mostRecentRightData = rightData.data


if __name__ == '__main__':
    try:
        # initialize ros node
        rospy.init_node('left_wheels')

        left_wheels = LeftWheels()
        left_wheels.run()
    except rospy.ROSInterruptException:
        pass
