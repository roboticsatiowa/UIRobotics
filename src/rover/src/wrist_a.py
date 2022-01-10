#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data)

def wrist_a():
    rospy.init_node('wrist_a')
    rospy.Subscriber('wrist_a',Int32,callback)
    rospy.spin()

if __name__ == '__main__':
    wrist_a()
