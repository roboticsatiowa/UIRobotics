#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Int32

left_data = 2**15
right_data = 2**15
pub_wrist_a = None
pub_wrist_b = None
angle = 0
rot = False

def publish(data):
    global pub_wrist_a
    global pub_wrist_b
    pub_wrist_a.publish(data[0])
    pub_wrist_b.publish(data[1])

def wrist_left(data):
    global left_data
    global right_data
    global rot
    global angle
    left_data = data.data
    rot = (left_data-2**15)*(right_data-2**15)<0
    if rot:
        publish([left_data,right_data])
    elif not rot and angle >= -90 and left_data < 2**15 and right_data < 2**15:
        publish([left_data,right_data])
    elif not rot and angle <= 90 and left_data > 2**15 and right_data > 2**15:
        publish([left_data,right_data])
    else:
        publish([2**15,2**15])

def wrist_right(data):
    global left_data
    global right_data
    global rot
    global angle
    right_data = data.data
    rot = (left_data-2**15)*(right_data-2**15)<0
    if rot:
        publish([left_data,right_data])
    elif not rot and angle >= -90 and left_data < 2**15 and right_data < 2**15:
        publish([left_data,right_data])
    elif not rot and angle <= 90 and left_data > 2**15 and right_data > 2**15:
        publish([left_data,right_data])
    else:
        publish([2**15,2**15])

def wrist_a_callback(data):
    global rot
    global angle
    global right_data
    global left_data
    if not rot:
        if right_data < 2**15 and left_data < 2**15:
            angle -= 360/68
        elif right_data > 2**15 and left_data > 2**15:
            angle += 360/68
        if angle > 90 or angle < -90:
            publish([2**15,2**15])
        print(angle)

def main():
    global pub_wrist_a
    global pub_wrist_b
    pub_wrist_a = rospy.Publisher('wrist_a',Int32,queue_size=10)
    pub_wrist_b = rospy.Publisher('wrist_b',Int32,queue_size=10)

    forwards = 0
    reverse = 2**16-1
    stopped = 2**15

    rospy.init_node('wrist_control')

    rate = rospy.Rate(10)

    rospy.Subscriber('wrist_left',Int32,wrist_left)
    rospy.Subscriber('wrist_right',Int32,wrist_right)

    rospy.Subscriber('wrist_a_encoder',Int32,wrist_a_callback)
    #rospy.Subscriber('wrist_b_encoder',Int32,wrist_b_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
