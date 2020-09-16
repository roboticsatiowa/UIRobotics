#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data)

def left_wheels():

    rospy.init_node('left_wheels')
    rospy.Subscriber('left_wheels', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    left_wheels()
