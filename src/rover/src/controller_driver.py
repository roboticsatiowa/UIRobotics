#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from inputs import get_gamepad
from time import sleep

def talker():

    maximum = (2**15 - 1)*10

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
    pub_xPos = rospy.Publisher('xPos',Int32,queue_size=10)
    pub_yPos = rospy.Publisher('yPos',Int32,queue_size=10)
    pub_zPos = rospy.Publisher('zPos',Int32,queue_size=10)

    pub_tilt = rospy.Publisher('tilt',Int32,queue_size=10)
    pub_rotate = rospy.Publisher('rotate',Int32,queue_size=10)
    pub_open = rospy.Publisher('open',Int32,queue_size=10)

    pub_right = rospy.Publisher('right_wheels',Int32,queue_size=10)
    pub_left = rospy.Publisher('left_wheels',Int32,queue_size=10)

    rospy.init_node('controller_driver')

    
    #while(pub_xPos.get_num_connections() == 0 or pub_yPos.get_num_connections() == 0 or pub_zPos.get_num_connections() == 0 or pub_tilt.get_num_connections() == 0 or pub_rotate.get_num_connections() == 0 or pub_open.get_num_connections() == 0 or pub_right.get_num_connections() == 0 or pub_left.get_num_connections() == 0):
        #print("No connection!")
    

    rate = rospy.Rate(10)

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
            
            if event.code == "RT" and mode == 2: #Call Program for Right Trigger
                o_hand += 5
            elif event.code == "LT" and mode == 2: #Call Program for Left Trigger
                o_hand -= 5
        
        #publish
        if mode == 0:
            pub_left.publish(y_left+2**15)
            pub_right.publish(y_right+2**15)
        elif mode == 1:
            x_arm += x_left
            y_arm += y_right
            z_arm += y_left

            if x_arm > maximum:
                x_arm = maximum
            elif x_arm < -maximum:
                x_arm = -maximum

            if y_arm > maximum:
                y_arm = maximum
            elif y_arm < -maximum:
                y_arm = -maximum

            if z_arm > maximum:
                z_arm = maximum
            elif z_arm < -maximum:
                z_arm = -maximum

            pub_xPos.publish(x_arm)
            pub_yPos.publish(y_arm)
            pub_zPos.publish(z_arm)
        elif mode == 2:
            pub_open.publish(o_hand)
            
            t_hand += y_left
            r_hand += y_right

            if t_hand > maximum:
                t_hand = maximum
            elif t_hand < -maximum:
                t_hand = -maximum

            if r_hand > maximum:
                r_hand = maximum
            elif r_hand < -maximum:
                r_hand = -maximum

            pub_tilt.publish(int(90*t_hand/maximum))
            pub_rotate.publish(int(90*r_hand/maximum))

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
