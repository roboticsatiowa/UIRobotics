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
#Channel A
#Github test

#GPIO.setup(15, GPIO.IN)
x=False
counter=0
counter2=0
y=0
motor1.duty_cycle = 0
motor2.duty_cycle = 0
while(True):
	motor1.duty_cycle = 0
	while(counter<=(343.5*4)):
		if(enc.value == True):
			counter += 1/12
			print(counter)
			while(enc.value == True):
				y+=1

	motor1.duty_cycle = 32767
	time.sleep(2)
	while(counter>=0):
		motor1.duty_cycle = 65535
		if(enc.value == True):
			counter -= 1/12
			print(counter)
			while(enc.value == True):
				y+=1
			
	motor1.duty_cycle = 32767
	time.sleep(2)

"""
time.sleep(2)
while(counter2>=35):
	if(enc2.value == True):
		counter2 += 1/12
		while(enc2.value == True):
			y+=1
"""


