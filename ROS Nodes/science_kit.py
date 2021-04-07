#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Int32

mode = 0

def mode_callback(data):
    global mode
    print("New mode:")
    mode = data.data
    print(mode)
    
def talker():
    
    global mode
    pub_cent = rospy.Publisher('centrifuge',Int32, queue_size=10)
    pub_pump = rospy.Publisher('pump',Int32, queue_size=10)
    rospy.init_node('science_kit')

    while(#insert subscriber nodes):
	print("No connection!")

    rospy.Subscriber('science_mode',Int32,mode_callback)
    
    rate = rospy.Rate(10)
    print("Talker initialized!")

    while not rospy.is_shutdown():

        
        rate.sleep()
 
  

if __name__ == '__main__':
    try:
        talker()
	
    except rospy.ROSInterruptException:
        pass
