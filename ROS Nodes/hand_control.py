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

status = 0

'''

0- stationary
1- rotating clockwise
2- rotating counterclockwise
3- turning right
4- turning left
5- opening
6- closing

'''

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

def wrist_a_callback(data):
    global status
    global c_w_angle
    global c_orientation_degree

    encoder_constant = ??? #number of encoder turns in a motor shaft turn
    gear_constant = ??? #number of motor shaft turns in a full join turn
    angle_constant = 360 / (encoder_constant * gear_constant) #joint angle change per encoder pulse

    if data.data == 1:
        if status == 1:
            c_orientation_degree = c_orientation_degree - angle_constant/2
        else if status == 2:
            c_orientation_degree = c_orientation_degree + angle_constant/2
        else if status == 3:
            c_w_angle = c_w_angle - angle_constant/2
        else if status == 4:
            c_w_angle = c_w_angle + angle_constant/2
        else:
            print("Unexpected motion!")

def wrist_b_callback(data):
    global status
    global c_w_angle
    global c_orientation_degree

    encoder_constant = ??? #number of encoder turns in a motor shaft turn
    gear_constant = ??? #number of motor shaft turns in a full join turn
    angle_constant = 360 / (encoder_constant * gear_constant) #joint angle change per encoder pulse

    if data.data == 1:
        if status == 1:
            c_orientation_degree = c_orientation_degree - angle_constant/2
        else if status == 2:
            c_orientation_degree = c_orientation_degree + angle_constant/2
        else if status == 3:
            c_w_angle = c_w_angle - angle_constant/2
        else if status == 4:
            c_w_angle = c_w_angle + angle_constant/2
        else:
            print("Unexpected motion!")

def gripper_callback(data):
    global status
    global c_grip_percent

    encoder_constant = ??? #number of encoder turns in a motor shaft turn
    gear_constant = ??? #number of motor shaft turns to fully open or close
    angle_constant = 100 / (encoder_constant * gear_constant) #joint angle change per encoder pulse

    if data.data == 1:
        if status == 5:
            c_grip_percent = c_grip_percent + angle_constant
        else if status == 6:
            c_grip_percent = c_grip_percent - angle_constant
        else:
            print("Gripper should not be moving. Something is wrong.")

def talker():
    global t_grip_percent
    global t_w_angle
    global t_orientation_degree
    global c_grip_percent
    global c_w_angle
    global c_orientation_degree
    global status
    
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
                status = 4
            else:
                #go backwards
                pub_wrist_a.publish(reverse)
                pub_wrist_b.publish(reverse)
                status = 3
        pub_wrist_a.publish(stopped)
        pub_wrist_b.publish(stopped)
        status =0 
        while abs(t_w_angle - c_w_angle > .5):
            if(t_w_angle > c_w_angle):
                #turn right
                pub_wrist_a.publish(forwards)
                pub_wrist_b.publish(reverse)
                status = 2
            else:
                #turn left
                pub_wrist_a.publish(reverse)
                pub_wrist_b.publish(forwards)
                status =1
        pub_wrist_a.publish(stopped)
        pub_wrist_b.publish(stopped)
        status =0
        while abs(t_grip_percent - c_grip_percent > .5):
            if(t_grip_percent > c_grip_percent):
                #close more
                pub_hand_grip.publish(forwards)
                status = 6
            else:
                #open more
                pub_hand_grip.publish(backwards)
                status = 5
        pub_hand_grip.publish(stopped)
        status = 0

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
