from inputs import get_gamepad

xDiff = 0
yDiff = 0
x = 0
y = 0 
b = 0
mode = 0 #0 is drive, 1 is arm, 2 is claw
rightTrig = 0
leftTrig = 0
while True:
    events = get_gamepad()
    
    for event in events:
        #print(event.ev_type, event.code, event.state)
        if event.code == "BTN_WEST": #Switch to drive mode
           mode = 0
        elif event.code == "BTN_NORTH": #Switch to arm mode
           mode = 1
        elif event.code == "BTN_EAST": #Switch to claw mode
           mode = 2 
        if event.code == "ABS_X" and -100 < xDiff + event.state/10000 < 100:
            xDiff = event.state/10000
        elif event.code == "ABS_Y" and -100 < yDiff + event.state/10000 < 100:
            yDiff = event.state/10000
        
        if event.code == "RT": #Call Program for Right Trigger
            rightTrig = 1
        elif event.code == "LT": #Call Program for Left Trigger
            leftTrig = 1
       
        if mode == 0:
            #Run Mode 1
        elif mode == 1:
            #Run Mode 2
        elif mode == 2:
            #Run Mode 3
       
        
        

    x += xDiff
    y += yDiff
    print(x,y)
