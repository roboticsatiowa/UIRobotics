#!/usr/bin/env python3
import board
import time
import rospy
from std_msgs.msg import Int32
from digitalio import DigitalInOut, Direction, Pull

def talker():
    pub_wrist = rospy.Publisher('wrist_a_encoder',Int32,queue_size=None)
    rospy.init_node('wrist_a_encoder')

    encoder_pin = board.D17

    enc = DigitalInOut(encoder_pin)
    enc.direction = Direction.INPUT
    enc.pull = Pull.UP

    rate = rospy.Rate(500)

    reset = True

    while not rospy.is_shutdown():

        if enc.value == True and reset:
            pub_wrist.publish(1)
            print("Encoder pulse")
            reset = False
        elif enc.value == False:
            reset = True

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
