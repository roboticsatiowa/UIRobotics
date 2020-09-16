#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

stopped = 32767
speed = 0 #robot speed, on a scale from 0-100
status = 0 #0 is stopped, 1 is fowards, 2 backwards, 3 left, 4 right

def status_callback():
    print("New status code:")
    rospy.loginfo(data.data)
    status = data.data

def speed_callback(data):
    print("New speed:")
    rospy.loginfo(data.data)
    speed = 32767*((data.data)/100)

def talker():
    pub_right = rospy.Publisher('right_wheels',Int16, queue_size=10)
    pub_left = rospy.Publisher('left_wheels',Int16, queue_size=10)
    rospy.init_node('wheel_control')
    rospy.Subscriber('speed',Int16,speed_callback)
    rospy.Subscriber('status',Int16,status_callback)
    rospy.spin()
    rate = rospy.Rate(10)
    

    while not rospy.is_shutdown():

        if(status==0):
            pub_right.publish(stopped)
            pub_left.publish(stopped)
        elif(status==1):
            pub_right.publish(stopped+speed)
            pub_left.publish(stopped+speed)
        elif(status==2):
            pub_right.publish(stopped-speed)
            pub_left.publish(stopped-speed)
        elif(status==3):
            pub_right.publish(stopped+speed)
            pub_left.publish(stopped-speed)
        elif(status==4):
            pub_right.publish(stopped-speed)
            pub_left.publish(stopped+speed)
        
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
