#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data)

def arm_shoulder():

    rospy.init_node('arm_shoulder')
    rospy.Subscriber('shoulder', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    arm_shoulder()
