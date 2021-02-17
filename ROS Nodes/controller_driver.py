#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from inputs import get_gamepad
from time import sleep

def talker():

    x_left = 0
    y_left = 0
    y_right = 0
    x_arm = 0
    y_arm = 0
    z_arm = 0
    t_hand = 0
    r_hand = 0
    o_hand = 0
    mode = 0 #0 is drive, 1 is arm, 2 is claw
    rightTrig = 0
    leftTrig = 0

    #create publishers

    rospy.init_node('gui')

    while(pub_speed.get_num_connections() == 0):
	print("No connection!")

    rate = rospy.Rate(10)

    print("Talker initialized!")

    while not rospy.is_shutdown():

        events = get_gamepad()

        for event in events
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
                print(y_left)
            elif event.code == "ABS_RY":
                y_right = event.state
            
            if event.code == "RT": #Call Program for Right Trigger
                rightTrig = 1
            elif event.code == "LT": #Call Program for Left Trigger
                leftTrig = 1
        
        #publish
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
