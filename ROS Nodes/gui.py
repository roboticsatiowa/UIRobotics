#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

speed = 50
status = 0

def talker():
    pub_speed = rospy.Publisher('speed',Int16,queue_size=10)
    pub_status = rospy.Publisher('speed',Int16,queue_size=10)

    rospy.init_node('gui')

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        pub_speed.publish(speed)
        pub_status.public(status)

        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
