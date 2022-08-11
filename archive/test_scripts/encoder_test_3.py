import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
from digitalio import DigitalInOut, Direction, Pull
enc = DigitalInOut(board.D27)
enc2 = DigitalInOut(board.D22)
enc.direction = Direction.INPUT
enc.direction = Direction.INPUT
enc.pull = Pull.UP
enc2.pull = Pull.UP

pca.frequency = 1000
motor1 = pca.channels[0]
motor2 = pca.channels[1]

while(True):
	print(enc.value)
