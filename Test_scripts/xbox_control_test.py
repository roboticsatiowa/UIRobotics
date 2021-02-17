from inputs import get_gamepad
from time import sleep

x_left = 0
y_left = 0
y_right = 0
x_arm = 0
y_arm = 0
z_arm = 0
mode = 0 #0 is drive, 1 is arm, 2 is claw
rightTrig = 0
leftTrig = 0
while True:

    if mode == 0:
        #Run Mode 1
        print(mode)
    elif mode == 1:
        x_arm += x_left
        y_arm += y_left
        z_arm += y_right
        print(x_arm,y_arm,z_arm)
    elif mode == 2:
        #Run Mode 3
        print(mode)
    
    sleep(.05)
    
    events = get_gamepad()
    
    for event in events:
        #print(event.ev_type, event.code, event.state)
        if event.code == "BTN_WEST": #Switch to drive mode
           mode = 0
           print("Drive mode")
        elif event.code == "BTN_NORTH": #Switch to arm mode
           mode = 1
           print("Arm mode")
        elif event.code == "BTN_EAST": #Switch to claw mode
           mode = 2
           print("Claw mode")
           
        if event.code == "ABS_X":
            x_left = event.state
        elif event.code == "ABS_Y":
            y_left = event.state
        elif event.code == "ABS_RY":
            y_right = event.state
        
        if event.code == "RT": #Call Program for Right Trigger
            rightTrig = 1
        elif event.code == "LT": #Call Program for Left Trigger
            leftTrig = 1

        

       
        #print(mode)
        

    
