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

print("Initialized!")

while True:
    events = get_gamepad()

    for event in events:
        if event.code == "ABS_Y":
            value = event.state + 2**15 - 1
            left.duty_cycle = value
            print("Left wheels set to: "+value)
        elif event.code == "ABS_RY":
            value = event.state + 2**15 - 1
            right.duty_cycle = value
            print("Right wheels set to: "+value)
