#!/usr/bin/env python
import rospy
import math
import time
from std_msgs.msg import Int32

#c for current, t for target
cHeading = 0 #degrees from east. TODO: use sensor to constantly update this
tHeading = 0
cLat = 100 #from GPS sensor
cLong = 20
tLat = 50
tLong = 10
autoMode = True

def talker():
    global autoMode
    global cHeading
    global tHeading
    global cLat
    global cLong
    global tLat
    global tLong

    pub_status = rospy.Publisher('status',Int32,queue_size=10)
    rospy.init_node('gps')

    while(pub_status.get_num_connections() == 0):
	print("No connection!")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        if autoMode:
            if tHeading > cHeading:
                pub_status.publish(3)
            elif tHeading < cHeading:
                pub_status.publish(4)
            else:
                pub_status.publish(1)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
	
    except rospy.ROSInterruptException:
        pass

