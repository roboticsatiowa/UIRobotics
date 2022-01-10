from inputs import get_gamepad
import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

pca.frequency = 1000
left = pca.channels[0]
right = pca.channels[1]
left_center = pca.channels[2]
right_center = pca.channels[3]
left_value = 0
right_value = 0

print("Initialized!")

while True:
    events = get_gamepad()

    for event in events:
        if event.code == "ABS_Y":
            left_value = event.state + 2**15 - 1
            print("Left wheels set to: "+left_value)
        elif event.code == "ABS_RY":
            right_value = event.state + 2**15 - 1
            print("Right wheels set to: "+right_value)
    if(left_value*right_value>=0):
        left.duty_cycle = left_value
        right.duty_cycle = right_value
        left_center.duty_cycle = left_value
        right_center.duty_cycle = right_value
    else:
        left.duty_cycle = left_value
        right.duty_cycle = right_value
        left_center.duty_cycle = int(left_value*0.712)
        right_center.duty_cycle = int(right_value*0.712)
