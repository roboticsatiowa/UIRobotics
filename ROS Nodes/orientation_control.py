#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data)

def orientation_control():
    rospy.init_node('orientation_control')
    rospy.Subscriber('orientation_control',Int32,callback)
    rospy.spin()

if __name__ == '__main__':
    orientation_control()