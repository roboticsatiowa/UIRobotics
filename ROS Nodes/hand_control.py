#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Int32

t_grip_percent = 0
t_w_angle = 0
t_orientation_degree = 0
c_grip_percent = 0
c_w_angle = 0
c_orientation_degree = 0

def grip_percent_callback(data):
    global t_grip_percent
    print("Target Grip Position: ")
    if data.data > 100:
        t_grip_percent = 100
    elif data.data < 0:
        t_grip_percent = 0
    else:
        t_grip_percent = data.data
    print(grip_percent)
def w_angle_callback(data):
    global t_w_angle
    print("Target wrist angle Postion: ")
    if data.data > 90:
        t_w_angle = 90
    elif data.data < -90:
        t_w_angle = -90
    else:
        t_w_angle = data.data
    print(w_angle)
def orientation_degree_callback(data):
    global t_orientation_degree
    print("Target Orientation: ")
    if data.data > 90:
        t_orientation_degree = 90
    elif data.data < -90:
        t_orientation_degree = -90
    else:
        t_orientation_degree = data.data
    print(orientation_degree)

#TODO: add callback functions

def talker():
    global t_grip_percent
    global t_w_angle
    global t_orientation_degree
    global c_grip_percent
    global c_w_angle
    global c_orientation_degree
    
    pub_hand_grip = rospy.Publisher('hand_grip',Int32,queue_size=10)
    pub_wrist_a = rospy.Publisher('wrist_a',Int32,queue_size=10)
    pub_wrist_b = rospy.Publisher('wrist_b',Int32,queue_size=10)

    forwards = 50000
    reverse = 65535 - forwards
    stopped = 32767

    rospy.init_node('hand_control')

    rate = rospy.Rate(10)

    while(pub_hand_grip.get_num_connections()==0 or pub_wrist_a.get_num_connections()==0 or pub_wrist_b.get_num_connections()==0):
        print("No connection!")

    rospy.Subscriber('grip_percent',Int32,grip_percent_callback)
    rospy.Subscriber('w_angle',Int32,w_angle_callback)
    rospy.Subscriber('orientation_degree',Int32,orientation_degree_callback)

    rospy.Subscriber('wrist_a_encoder',Int32,wrist_a_callback)
    rospy.Subscriber('wrist_b_encoder',Int32,wrist_b_callback)
    rospy.Subscriber('gripper_encoder',Int32,gripper_callback)

    while not rospy.is_shutdown():
        while abs(t_orientation_degree - c_orientation_degree > .5):
            if(t_orientation_degree > c_orientation_degree):
                #go forwards
                pub_wrist_a.publish(forwards)
                pub_wrist_b.publish(forwards)
            else:
                #go backwards
                pub_wrist_a.publish(reverse)
                pub_wrist_b.publish(reverse)
        pub_wrist_a.publish(stopped)
        pub_wrist_b.publish(stopped)
        while abs(t_w_angle - c_w_angle > .5):
            if(t_w_angle > c_w_angle):
                #turn right
                pub_wrist_a.publish(forwards)
                pub_wrist_b.publish(reverse)
            else:
                #turn left
                pub_wrist_a.publish(reverse)
                pub_wrist_b.publish(forwards)
        pub_wrist_a.publish(stopped)
        pub_wrist_b.publish(stopped)
        while abs(t_grip_percent - c_grip_percent > .5):
            if(t_grip_percent > c_grip_percent):
                #close more
                pub_hand_grip.publish(forwards)
            else:
                #open more
                pub_hand_grip.publish(backwards)
        pub_hand_grip.publish(stopped)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
