# Creates a visual window for testing/debugging of the controller

import pygame
from xboxController import getInputs

background_colour = (255,255,255)
window_size = (400, 200)

# initialize pygame window which can be referenced with screen variable
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Controller Axis Test')

# checks for the window X button clicked and exits the program
def checkExit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# draw to the pygame window
def draw():
    # dictionary of controller input states
    inputs = getInputs(pygame.joystick.Joystick(0))
    
    screen.fill(background_colour)
    
    # draw joystick circles
    pygame.draw.circle(screen, (0,0,0), (inputs['Lstick_x']*30 + 100, -inputs['Lstick_y']*30 + 100), 5)
    pygame.draw.circle(screen, (0,0,0), (inputs['Rstick_x']*30 + 300, -inputs['Rstick_y']*30 + 100), 5)
    
    # draw trigger rectangles
    Rtrig, Ltrig = inputs['Rtrig']*75 + 5, inputs['Ltrig']*75 + 5
    pygame.draw.rect(screen, (0,0,0), pygame.rect.Rect(20, 150-Ltrig, 10, Ltrig))
    pygame.draw.rect(screen, (0,0,0), pygame.rect.Rect(380, 150-Rtrig, 10, Rtrig))

# continuously updates screen and checks for exit conditions
def main():
    while True:
        checkExit()
        draw()
        pygame.display.flip()
        
if __name__ == '__main__':
    main()
