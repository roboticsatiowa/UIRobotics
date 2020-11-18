import math
import pygame
import time
t_xPos = 0.3
t_yPos = 0.3
t_zPos = .3
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

alpha= math.acos((math.pow(u_sec,2)+math.pow(l_sec,2)-math.pow(d_d,2))/(2*l_sec*u_sec))

#te_angle = math.acos(math.pow(d_d,2)-math.pow(l_sec,2)-math.pow(u_sec,2))/(2*l_sec*u_sec)) #this is in radians

te_angle = math.pi - alpha

ts_angle = math.degrees(math.atan(h_d/t_zPos)+math.atan((u_sec*math.sin(te_angle))/(l_sec+u_sec*math.cos(te_angle)))) #target elbow angle

te_angle = math.degrees(te_angle) #convert to degrees

print(tb_angle,ts_angle,te_angle)

pygame.init()

screen_width =500
screen_height = 500
screen_center = (screen_width / 2, screen_height / 2)

screen = pygame.display.set_mode([screen_width, screen_height])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen,(66,135,245),(int(screen_width/2),int(screen_height/2)),6)

    pygame.draw.circle(screen,(199,38,81),(int(screen_center[0]+h_d*250),int(screen_center[1]-t_zPos*250)),6)

    pygame.draw.line(screen,0,(screen_center[0],screen_center[1]),(screen_center[0]+250*(l_sec*math.cos(math.radians(ts_angle))),screen_center[1]-250*(l_sec*math.sin(math.radians(ts_angle)))),4)

    pygame.draw.line(screen,0,(screen_center[0]+250*(l_sec*math.cos(math.radians(ts_angle))),screen_center[1]-250*(l_sec*math.sin(math.radians(ts_angle)))),(screen_center[0]+250*(u_sec*math.cos(math.radians(te_angle))),screen_center[1]-250*(u_sec*math.sin(math.radians(te_angle)))),4)

    #pygame.draw.line(screen,0,(screen_center[0],screen_center[1]),(screen_center[0]+250,screen_center[1]-250))

    pygame.display.flip()

    pygame.display.flip()

pygame.quit()
