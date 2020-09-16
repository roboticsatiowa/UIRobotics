#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

def callback(data):
    rospy.loginfo(data.data)

def arm_elbow():

    rospy.init_node('arm_elbow')
    rospy.Subscriber('elbow', Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    arm_elbow()
