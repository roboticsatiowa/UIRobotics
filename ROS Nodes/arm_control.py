#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

def talker():

    pub_base = rospy.Publisher('base',Int16,queue_size=10)
    
    pub_shoulder = rospy.Publisher('shoulder',Int16,queue_size=10)

    pub_elbow = rospy.Publisher('elbow',Int16,queue_size=10)

    rospy.init_node('wheel_control')
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        #publish to base, shoulder, elbow

        rate.sleep()

    if __name__ == '__main__':
        try:
            talker()
        except rospy.ROSInterruptException:
            pass
