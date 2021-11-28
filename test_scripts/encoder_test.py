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


#GPIO.setup(15, GPIO.IN)
x=False
counter=0
counter2=0
y=0
motor1.duty_cycle = 0
motor2.duty_cycle = 0
while(1==1):

	#print(enc.value)
	#time.sleep(.1)

	
	if((enc.value == True)and(enc2.value == False)):
		counter += 1/12
		#print(counter)
		while((enc.value == True)and(enc2.value == False)):
			y+=1

	if((enc.value == True)and(enc2.value == True)):
		counter += 1/12
		counter2 += 1/12
		while((enc.value == True)and(enc2.value == True)):
			y+=1

	if((enc.value == False)and(enc2.value == True)):
		counter2 += 1/12
		while((enc.value == False)and(enc2.value == True)):
			y+=1

	if(counter>=99.5):
		motor1.duty_cycle = 32767

	if(counter2>=139):
		motor2.duty_cycle = 32767
	
