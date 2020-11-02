#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Int32

hand_grip = 0
w_angle = 90
orientation = 0

def hand_grip_callback(data):
    global hand_grip
    print("Target Grip Position: ")
    hand_grip = data.data
    print(hand_grip)
def w_angle_callback(data):
    global w_angle
    print("Target wrist angle Postion: ")
    w_angle = data.data
    print(w_angle)
def orientation_callback(data):
    global orientation
    print("Target Orientation: ")
    orientation = data.data
    print(orientation)

def talker():
    global hand_grip
    global w_angle
    global orientation
    pub_hand_control = rospy.Publisher('hand_control',Int32,queue_size=10)
    pub_wrist_control = rospy.Publihser('wrist_control',Int32,queue_size=10)
    pub_orientation_control = rospy.Publisher('orientation_control',Int32,queue_size=10)

    rospy.init_node('hand_control')

    rate = rospy.Rate(10)

    while(pub_hand_control.get_num_connections()==0 or pub_wrist_control.get_num_connections()==0 or pub_orientation_control.get_num_connections()==0):
        print("No connection!")

    rospy.Subscriber('hand_grip',Int32,hand_grip_callback)
    rospy.Subscriber('w_angle',Int32,w_angle_callback)
    rospy.Subscriber('orientation',Int32,orientation_callback)

    while not rospy.is_shutdown():
        