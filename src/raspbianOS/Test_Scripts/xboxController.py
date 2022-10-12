import pygame
import os
from time import sleep

pygame.init()
xboxController = pygame.joystick.Joystick(0)

def getInputs(controller:pygame.joystick.Joystick) -> dict:
    '''Returns a dict of each button mapped to its value'''
    return {
            "B": bool(controller.get_button(1)),
            "A": bool(controller.get_button(0)),
            "X": bool(controller.get_button(2)),
            "Y": bool(controller.get_button(3)),
            "LB": bool(xboxController.get_button(4)),
            "RB": bool(controller.get_button(5)),
            "BACK": bool(controller.get_button(6)),
            "START": bool(controller.get_button(7)),
            "Lstick_pressed": bool(controller.get_button(8)),
            "Rstick_pressed": bool(controller.get_button(9)),
            "Lstick_x": round(controller.get_axis(0), 3),
            "Lstick_y": round(-controller.get_axis(1), 3), #  value inverted so forward is positive
            "Rstick_x": round(controller.get_axis(2), 3),
            "Rstick_y": round(-controller.get_axis(3), 3), # value inverted so forward is positive
            "Ltrig": round((controller.get_axis(4)+1)/2, 3), # value mapped from (-1.0, 1.0) to (0.0, 1.0)
            "Rtrig": round((controller.get_axis(5)+1)/2, 3), # value mapped from (-1.0, 1.0) to (0.0, 1.0)
            "dPad_x": controller.get_hat(0)[0], # TODO still not sure how to get D pad values
            "dPad_y": controller.get_hat(0)[1], # 
        }

def display():
    while True:
         # updates the controller input values
        pygame.event.get()
        controlMap = getInputs(xboxController)
            
        # clears the screen every frame. should work on both linux and windows
        os.system('cls' if os.name=='nt' else 'clear')
        
        # print each controller input with its value
        s = ''
        for item in controlMap:
            s = '{}\n{}: {}'.format(s, str(item), str(controlMap[item]))
        print(s)
        
        # hacky solution to reduce screen flickering
        # NOTE: this creates latency so the values shown in the console do not reflect actual response times
        sleep(0.05)
        
        
if __name__ == '__main__':
    display()