import pygame
from pygame.joystick import Joystick


class XBcontroller():
    buttons = {
        0: 'A',
        1: 'B',
        2: 'X',
        3: 'Y',
        4: 'LB',
        5: 'RB',
        6: 'BCK',
        7: 'STA',
        8: 'LST',
        9: 'RST',
    }

    axes = {
        0: 'LX',
        1: 'LY',
        2: 'RX',
        3: 'RY',
        4: 'LT',
        5: 'RT',
    }

    def __init__(self):
        self.joystick = pygame.joystick.Joystick(0)

    def update(self) -> None:
        self.A = bool(self.joystick.get_button(0))
        self.B = bool(self.joystick.get_button(1))
        self.X = bool(self.joystick.get_button(2))
        self.Y = bool(self.joystick.get_button(3))
        self.LB = bool(self.joystick.get_button(4))
        self.RB = bool(self.joystick.get_button(5))
        self.BACK = bool(self.joystick.get_button(6))
        self.START = bool(self.joystick.get_button(7))
        self.DPAD_S = self.joystick.get_hat(0)[1] == -1
        self.DPAD_E = self.joystick.get_hat(0)[0] == -1
        self.DPAD_W = self.joystick.get_hat(0)[0] == 1
        self.DPAD_N = self.joystick.get_hat(0)[1] == 1
        self.LSTICK = bool(self.joystick.get_button(8))
        self.RSTICK = bool(self.joystick.get_button(10))
        self.LSTICK_X = self.joystick.get_axis(0)
        self.LSTICK_Y = self.joystick.get_axis(1)
        self.RSTICK_X = self.joystick.get_axis(3)
        self.RSTICK_Y = self.joystick.get_axis(4)
        self.LTRIG = self.joystick.get_axis(2)
        self.RTRIG = self.joystick.get_axis(5)

    def getInput(self, event: pygame.event.Event):
        if not (1535 < event.type < 1543):
            return None
        self.update()
        if event.type == 1536:  # AXIS CHANGED (Sticks and Triggers)
            return f"AXIS_CHANGED: {self.axes[event.dict['axis']]} {event.dict['value']}"
        if event.type == 1538:  # HAT CHANGED (D-Pad)
            return f"HAT_CHANGED: {event.dict['value']}"
        if event.type == 1539:  # BUTTON PRESSED
            return f"PRESSED {self.buttons[event.dict['button']]}"
        if event.type == 1540:  # BUTTON RELEASED
            return f"RELEASED {self.buttons[event.dict['button']]}"
        if event.type == 1541:
            self.joystick = pygame.joystick.Joystick(0)
            return 'JOY_DEVICE_ADDED'
        if event.type == 1542:
            return 'JOY_DEVICE_REMOVED'


if __name__ == '__main__':
    pygame.init()
    cont = XBcontroller()

    # Continuosly check for pygame updates
    while True:
        events = pygame.event.get()
        for event in events:  # allows multiple events to be handled at once
            print(cont.getInput(event))
