#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def talker():

    #create publishers

    rospy.init_node('gui')

    while(pub_speed.get_num_connections() == 0):
	print("No connection!")

    rate = rospy.Rate(10)

    print("Talker initialized!")

    while not rospy.is_shutdown():
        #publish
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
