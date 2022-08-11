#!/usr/bin/env python3
import board
import busio
import time
import adafruit_pca9685
import rospy
from std_msgs.msg import Int32
from digitalio import DigitalInOut, Direction, Pull

def talker():
    pub_gripper = rospy.Publisher('gripper_encoder',Int32,queue_size=10)
    rospy.init_node('gripper_encoder')

    i2c = busio.I2C(board.SCL,board.SDA)
    pca = adafruit_pca9685.PCA9685(i2c)

    encoder_pin = #encoder pin

    enc = DigitalInOut(encoder_pin)
    enc.direction = Direction.INPUT
    enc.pull = Pull.UP

    pca.frequency = 1000

    rate = rospy.Rate(10)

    reset = True

    while not rospy.is_shutdown():

        if enc.value == True and reset:
            pub_gripper.publish(1)
            reset = False
        else if enc.value == False:
            reset = True

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
