#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

speed = 50
status = 3

def talker():
    global speed
    pub_speed = rospy.Publisher('speed',Int32,queue_size=10)
    pub_status = rospy.Publisher('status',Int32,queue_size=10)
    pub_xPos = rospy.Publisher('t_xPos',Int32,queue_size=10)
    pub_yPos = rospy.Publisher('t_yPos',Int32,queue_size=10)
    pub_zPos = rospy.Publisher('t_zPos',Int32,queue_size=10)

    rospy.init_node('gui')

    while(pub_speed.get_num_connections() == 0):
	print("No connection!")

    rate = rospy.Rate(10)

    print("Talker initialized!")

    while not rospy.is_shutdown():

        key = raw_input("New speed (out of 100):")

	speed = int(key)

        pub_speed.publish(speed)

        pub_status.publish(status)

        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
