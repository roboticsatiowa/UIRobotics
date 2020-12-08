#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

speed = 50
status = 3
grip_percent = 0
w_angle = 90
orientation_degree = 0

def talker():
    global speed
    global w_angle
    global grip_percent
    global orientaion_degree
    pub_speed = rospy.Publisher('speed',Int32,queue_size=10)
    pub_status = rospy.Publisher('status',Int32,queue_size=10)
    pub_xPos = rospy.Publisher('t_xPos',Int32,queue_size=10)
    pub_yPos = rospy.Publisher('t_yPos',Int32,queue_size=10)
    pub_zPos = rospy.Publisher('t_zPos',Int32,queue_size=10)
    pub_grip = rospy.Publisher('grip_percent',Int32,queue_size=10)
    pub_angle = rospy.Publisher('w_angle',Int32,queue_size=10)
    pub_orientation = rospy.Publisher('orientation_degree',Int32,queue_size=10)

    rospy.init_node('gui')

    while(pub_speed.get_num_connections() == 0):
	print("No connection!")

    rate = rospy.Rate(10)

    print("Talker initialized!")

    while not rospy.is_shutdown():

        key = raw_input("New speed (out of 100):")
        grip_key = raw_input("amount of closure of hand (out of 100):")
        w_key = raw_input("angle of wrist perpendicular to the arm(0 to 180):")
        o_key = raw_input("orientation of the hand(0 to 360):")

	speed = int(key)
        grip_percent = int(grip_key)
        orientation_degree = int(o_key)
        w_angle = int(w_key)
        
        pub_speed.publish(speed)

        pub_status.publish(status)

        pub_orientation.publish(orientation_degree)

        pub_grip.publish(grip_percent)

        pub_angle.publish(w_angle)

        rate.sleep()
    


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
