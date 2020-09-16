#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

forwards = 100
backwards = 0
stopped = 50

def talker():
    pub_right = rospy.Publisher('right_wheels',Int16, queue_size=10)
    pub_left = rospy.Publisher('left_wheels',Int16, queue_size=10)
    rospy.init_node('wheel_control')
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        key = raw_input("W- Forward; S- Backwards; A- Left; D- Right")

        if(key=="W"):
            pub_right.publish(forwards)
            pub_left.publish(forwards)
        elif(key=="S"):
            pub_right.publish(backwards)
            pub_left.publish(backwards)
        elif(key=="A"):
            pub_right.publish(forwards)
            pub_left.publish(backwards)
        elif(key=="D"):
            pub_right.publish(backwards)
            pub_left.publish(forwards)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
