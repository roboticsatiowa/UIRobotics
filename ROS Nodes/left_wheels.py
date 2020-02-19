#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(data.data)

def left_wheels():

    rospy.init_node('left_wheels')
    rospy.Subscriber('left_wheels', Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    left_wheels()
