import math
t_xPos = .3
t_yPos = .3
t_zPos = .8
b_angle = 0 #angles are in degrees, not radians
s_angle = 0
e_angle = 0
l_sec = .5 # lower arm section, the one closest to the base
u_sec = .5
speed = 100 #movement speed 1-100
tb_angle = 0
ts_angle = 0
te_angle = 0

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
'''
while abs(b_angle-tb_angle)>.5:
    if b_angle < tb_angle:
        #pub_base.publish(signal)
        print("base pos")
    else:
        #pub_base.publish(reverse)
        print("base neg")

while abs(s_angle-ts_angle)>.5:
    if s_angle < ts_angle:
        #pub_shoulder.publish(signal)
        print("shoulder pos")
    else:
        #pub_shoulder.publish(reverse)
        print("shoulder neg")

while abs(e_angle-te_angle)>.5:
    if e_angle < te_angle:
        #pub_elbow.publish(signal)
        print("elbow pos")
    else:
        #pub_elbow.publish(reverse)
        print("elbow neg")
'''
