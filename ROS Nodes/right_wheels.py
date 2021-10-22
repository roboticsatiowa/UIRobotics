#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data)

def right_wheels():

    rospy.init_node('right_wheels')
    rospy.Subscriber('right_wheels', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    right_wheels()
