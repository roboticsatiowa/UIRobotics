#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data.data)

def hand_grip():
    rospy.init_node('hand_grip')
    rospy.Subscriber('hand_grip',Int32,callback)
    rospy.spin()

if __name__ == '__main__':
    hand_grip()
