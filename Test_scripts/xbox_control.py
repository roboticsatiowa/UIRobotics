from inputs import get_gamepad

xDiff = 0
yDiff = 0
x = 0
y = 0 
while True:
    events = get_gamepad()
    
    for event in events:
        #print(event.ev_type, event.code, event.state)
        if event.code == "ABS_X" and -100 < xDiff + event.state/10000 < 100:
            xDiff = event.state/10000
        elif event.code == "ABS_Y" and -100 < yDiff + event.state/10000 < 100:
            yDiff = event.state/10000

    x += xDiff
    y += yDiff
    print(x,y)
