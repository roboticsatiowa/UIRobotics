import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
from digitalio import DigitalInOut, Direction, Pull
#enc = DigitalInOut(board.D27)
left = DigitalInOut(board.D22)
rightButton = DigitalInOut(board.D25)

#enc.direction = Direction.INPUT
left.direction = Direction.INPUT
rightButton.direction = Direction.INPUT
#enc.pull = Pull.UP
left.pull = Pull.UP
rightButton.pull = Pull.UP

pca.frequency = 1000
led_channel = pca.channels[0]
led_channel.duty_cycle = 32767

print("Ready!")

while(1==1):

	if((left.value==False)and(rightButton.value==True)):
		led_channel.duty_cycle = 0xffff
		print("Right")
	elif((left.value==True)and(rightButton.value==False)):
		led_channel.duty_cycle = 0
		print("Left")
	else:
		led_channel.duty_cycle = 32767
