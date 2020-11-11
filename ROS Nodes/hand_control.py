#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Int32

grip_percent = 0
w_angle = 90
orientation_degree = 0

def grip_percent_callback(data):
    global grip_percent
    print("Target Grip Position: ")
    grip_percent = data.data
    print(grip_percent)
def w_angle_callback(data):
    global w_angle
    print("Target wrist angle Postion: ")
    w_angle = data.data
    print(w_angle)
def orientation_degree_callback(data):
    global orientation_degree
    print("Target Orientation: ")
    orientation_degree = data.data
    print(orientation_degree)

def talker():
    global grip_percent
    global w_angle
    global orientation_degree
    pub_hand_grip = rospy.Publisher('hand_grip',Int32,queue_size=10)
    pub_wrist_control = rospy.Publihser('wrist_control',Int32,queue_size=10)
    pub_orientation_control = rospy.Publisher('orientation_control',Int32,queue_size=10)

    rospy.init_node('hand_control')

    rate = rospy.Rate(10)

    while(pub_hand_grip.get_num_connections()==0 or pub_wrist_control.get_num_connections()==0 or pub_orientation_control.get_num_connections()==0):
        print("No connection!")

    rospy.Subscriber('grip_percent',Int32,grip_percent_callback)
    rospy.Subscriber('w_angle',Int32,w_angle_callback)
    rospy.Subscriber('orientation_degree',Int32,orientation_degree_callback)

    while not rospy.is_shutdown():
        


