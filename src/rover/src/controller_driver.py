#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from inputs import get_gamepad
from time import sleep

def talker():

    mode = 0 #0 is drive, 1 is arm, 2 is claw
    rightTrig = 0
    leftTrig = 0

    #create publishers
    pub_xPos = rospy.Publisher('xPos',Int32,queue_size=None)
    pub_yPos = rospy.Publisher('yPos',Int32,queue_size=None)
    pub_zPos = rospy.Publisher('zPos',Int32,queue_size=None)

    pub_right = rospy.Publisher('right_wheels',Int32,queue_size=None)
    pub_left = rospy.Publisher('left_wheels',Int32,queue_size=None)

    right_wrist = rospy.Publisher('wrist_right',Int32,queue_size=None)
    left_wrist = rospy.Publisher('wrist_left',Int32,queue_size=None)

    rospy.init_node('controller_driver')

    rate = rospy.Rate(50)

    print("Talker initialized!")

    while not rospy.is_shutdown():

        events = get_gamepad()

        for event in events:
            #print(event.ev_type, event.code, event.state)
            if event.code == "BTN_WEST": #Switch to drive mode
               mode = 0
               print("Drive mode")
            elif event.code == "BTN_NORTH": #Switch to arm mode
               mode = 1
               print("Arm mode")
            elif event.code == "BTN_EAST": #Switch to claw mode
               mode = 2
               print("Claw mode")
               
            if event.code == "ABS_X":
                x_left = event.state
            elif event.code == "ABS_Y":
                y_left = event.state
            elif event.code == "ABS_RY":
                y_right = event.state
        
        #publish
        if mode == 0:
            pub_left.publish(y_left+2**15)
            pub_right.publish(y_right+2**15)
        elif mode == 1:
            #arm input
        elif mode == 2:
            left_wrist.publish(y_left+2**15)
            right_wrist.publish(y_right+2**15)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
