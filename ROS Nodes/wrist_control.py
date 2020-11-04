#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32


def callback(data):
    rospy.loginfo(data.data)

def wrist_control():
    rospy.init_node('wrist_control')
    rospy.Subscriber('wrist_control',Int32,callback)
    rospy.spin()

if __name__ == '__main__':
    wrist_control()