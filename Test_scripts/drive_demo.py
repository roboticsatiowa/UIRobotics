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

while True:
    events = get_gamepad()

    for event in events:
        if event.code == "ABS_Y":
            left.duty_cycle = event.state + 2**15 - 1
        elif event.code == "ABS_RY":
            right.duty_cycle = event.state + 2**15 - 1
