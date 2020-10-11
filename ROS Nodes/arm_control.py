#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Int32

t_xPos = 0
t_yPos = 0
t_zPos = 0
b_angle = 0 #angles are in degrees, not radians
s_angle = 0
e_angle = 0
l_sec = 5 # lower arm section, the one closest to the base
u_sec = 5
speed = 100 #movement speed 1-100

def t_xPos_callback(data):
    global t_xPos
    print("Target X Position: ")
    t_xPos = data.data
    print(t_xPos)

def t_yPos_callback(data):
    global t_yPos
    print("Target Y Position: ")
    t_yPos = data.data
    print(t_yPos)

def t_zPos_callback(data):
    global t_zPos
    print("Target Z Position: ")
    t_zPos = data.data
    print(t_zPos)


def talker():
    global t_xPos
    global t_yPos
    global t_zPos
    global b_angle #TODO: Add feedback from encoders to update these
    global s_angle
    global e_angle
    global l_sec
    global u_sec
    global speed
    tb_angle = 0
    ts_angle = 0
    te_angle = 0
    
    pub_base = rospy.Publisher('base',Int32,queue_size=10)
    
    pub_shoulder = rospy.Publisher('shoulder',Int32,queue_size=10)

    pub_elbow = rospy.Publisher('elbow',Int32,queue_size=10)

    rospy.init_node('arm_control')

    while(pub_base.get_num_connections()==0 or pub_shoulder.get_num_connections()==0 or pub_elbow.get_num_connections()==0):
        print("No connection!")

    rospy.Subscriber('t_xPos',Int32,t_xPos_callback)
    rospy.Subscriber('t_yPos',Int32,t_yPos_callback)
    rospy.Subscriber('t_zPos',Int32,t_zPos_callback)
    
    
    rate = rospy.Rate(10)
    print("Talker initialized!")

    while not rospy.is_shutdown():

        signal = (speed/100)*65535
        reverse = signal * -1

        if pow(pow(t_xPos,2)+pow(t_yPos,2)+pow(t_zPos,2),.5)>l_sec+u_sec:
            print("WARNING: Out of reach!")

        #calculate target angles

        h_d = math.pow((math.pow(t_xPos,2)+math.pow(t_yPos,2)),.5) #horizontal distance between arm base and target

        tb_angle_temp = math.degrees(math.acos(t_xPos/h_d)) #set target base angle

        #print(tb_angle_temp)
        if t_xPos < 0:
            #print("target to left of arm")
            tb_angle = tb_angle_temp #if target is to the left of the arm need to do this
            #print(tb_angle,tb_angle_temp)
        else:
            tb_angle = tb_angle_temp

        d_d = math.pow((math.pow(h_d,2)+math.pow(t_zPos,2)),.5) #diagonal distance calculation

        te_angle = math.acos((math.pow(h_d,2)+math.pow(t_zPos,2)-math.pow(l_sec,2)-math.pow(u_sec,2))/(2*l_sec*u_sec)) #this is in radians

        ts_angle = math.degrees(math.atan(h_d/t_zPos)-math.atan((u_sec*math.sin(te_angle))/(l_sec+u_sec*math.cos(te_angle)))) #target elbow angle

        te_angle = math.degrees(te_angle) #convert to degrees

        print(tb_angle,ts_angle,te_angle)

        #move to match target angles

        while abs(b_angle-tb_angle)>.5:
            if b_angle < tb_angle:
                #pub_base.publish(signal)
            else:
                #pub_base.publish(reverse)

        while abs(s_angle-ts_angle)>.5:
            if s_angle < ts_angle:
                #pub_shoulder.publish(signal)
            else:
                #pub_shoulder.publish(reverse)

        while abs(e_angle-te_angle)>.5:
            if e_angle < te_angle:
                #pub_elbow.publish(signal)
            else:
                #pub_elbow.publish(reverse)
            
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
