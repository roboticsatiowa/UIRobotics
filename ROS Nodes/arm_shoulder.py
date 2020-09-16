#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(data.data)

def arm_shoulder():

    rospy.init_node('arm_shoulder')
    rospy.Subscriber('shoulder', Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    arm_shoulder()
