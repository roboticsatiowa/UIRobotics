#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, Bool
from inputs import get_gamepad
from time import sleep

class ControllerDriver():
    def __init__(self):
        self.y_left = 0
        self.y_right = 0
        self.enabled = False

        # ros pub and subs
        self.pub_right = rospy.Publisher('right_wheels',Int32,queue_size=None)
        self.pub_left = rospy.Publisher('left_wheels',Int32,queue_size=None)
        self.pub_enabled = rospy.Publisher('enabled', Bool, queue_size=1)

        self.rate = rospy.Rate(50)

    def talk(self):
         while not rospy.is_shutdown():

            events = get_gamepad()

            for event in events:
                # get gamepad stick y positions
                if event.code == "ABS_Y":
                    y_left = event.state
                elif event.code == "ABS_RY":
                    y_right = event.state

                # set drive mode 
                if event.code == "BTN_NORTH":
                    self.enabled = True
                    rospy.loginfo("Drive mode ENABLED")
                elif event.code == "BTN_EAST": 
                    self.enabled = False
                    rospy.loginfo("Drive mode DISABLED")
                
            #publish
            self.pub_left.publish(y_left + 2**15)
            self.pub_right.publish(y_right + 2**15)
            self.pub_enabled.publish(self.enabled)

            self.rate.sleep()

if __name__ == '__main__':
    try:
        # initialize ros node
        rospy.init_node('controller_driver')

        controller_driver = ControllerDriver()
        controller_driver.talk()
    except rospy.ROSInterruptException:
        pass
