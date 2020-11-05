import math
import pygame

def ik(xPos,yPos,seg1 = 1, seg2 = 1):
    
    upperAngle = math.acos((-math.pow(seg1,2)-math.pow(seg2,2)+math.pow(xPos,2)+math.pow(yPos,2))/(2*seg1*seg2))
    
    lowerAngle = math.atan2(yPos,xPos) - math.atan2((seg2*math.sin(upperAngle)),(seg1+seg2*math.cos(upperAngle)))

    print(math.degrees(lowerAngle),math.degrees(upperAngle))

    pygame.init()

    screen_width =500
    screen_height = 500
    screen_center = (screen_width / 2, screen_height / 2)

    screen = pygame.display.set_mode([screen_width, screen_height])

    count = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen,(66,135,245),(int(screen_width/2),int(screen_height/2)),6)

        pygame.draw.circle(screen,(199,38,81),(int(screen_center[0]+xPos*100),int(screen_center[1]-yPos*100)),6)


        seg1Pos = (int(screen_center[0] + 100*seg1*math.cos(lowerAngle)),int(screen_center[1] - 100*seg1*math.sin(lowerAngle)))

        seg2Pos = (int(screen_center[0] + 100*seg2*math.cos(upperAngle)+seg1Pos[0]),int(screen_center[1] - 100*seg2*math.sin(upperAngle)-seg1Pos[1]))

        pygame.draw.circle(screen,(227, 54, 224),seg1Pos,6)

        pygame.draw.circle(screen,(56, 219, 50),seg2Pos,6)

        if count == 0:
            print((int(screen_center[0]+xPos*100),int(screen_center[1]-yPos*100)))
            print(seg1Pos,seg2Pos)
            count = count + 1

        pygame.draw.line(screen,0,screen_center,seg1Pos,4)

        pygame.draw.line(screen,0,seg1Pos,seg2Pos,4)

        #pygame.draw.line(screen,0,screen_center,(int(screen_center[0]+xPos*100),int(screen_center[1]-yPos*100)),4)

        pygame.display.flip()


    pygame.quit()


ik(1,0.5)
