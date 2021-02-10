from inputs import get_gamepad

xDiff = 0
yDiff = 0
x = 0
y = 0 
b = 0
mode = 0
righTrig = 0
leftTrig = 0
while True:
    events = get_gamepad()
    
    for event in events:
        #print(event.ev_type, event.code, event.state)
        if event.code == "ABS_X" and -100 < xDiff + event.state/10000 < 100:
            xDiff = event.state/10000
        elif event.code == "ABS_Y" and -100 < yDiff + event.state/10000 < 100:
            yDiff = event.state/10000
        elif event.code == "ABS_B": #Call Program for b:
           mode = 2 
        elif event.code == "RT": #Call Program for Right Trigger
            #Output
        elif event.code == "LT": #Call Program for Left Trigger
            #Output
       
        if mode == 0:
            #Run Mode 1
        elif mode == 1:
            #Run Mode 2
        elif mode == 2:
            #Run Mode 3
       
        
        

    x += xDiff
    y += yDiff
    print(x,y)
