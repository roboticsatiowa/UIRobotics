#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Int32

stopped = 32767
speed = 0#robot speed, on a scale from 0-100
status = 0#0 is stopped, 1 is fowards, 2 backwards, 3 left, 4 right



def status_callback(data):
    global status
    print("New status code:")
    #rospy.loginfo(data.data)
    status = data.data
    print(status)

def speed_callback(data):
    global speed
    speed = int(32767*(float(data.data)/100))
    print("New speed:")
    print(speed)
    #rospy.loginfo(data.data)
    

def talker():
    
    global stopped
    global status
    global speed
    pub_right = rospy.Publisher('right_wheels',Int32, queue_size=10)
    pub_left = rospy.Publisher('left_wheels',Int32, queue_size=10)
    rospy.init_node('wheel_control')

    while(pub_right.get_num_connections()==0 or pub_left.get_num_connections() ==0):
	print("No connection!")

    rospy.Subscriber('speed',Int32,speed_callback)
    rospy.Subscriber('status',Int32,status_callback)
    
    
    rate = rospy.Rate(10)
    print("Talker initialized!")

    
    

    while not rospy.is_shutdown():

	#print("publishing!")

        if(status==0):
            pub_right.publish(stopped)
            pub_left.publish(stopped)
	    #print("published!")
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
