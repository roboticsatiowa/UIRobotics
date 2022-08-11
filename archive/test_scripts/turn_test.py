import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

pca.frequency = 1000
right = pca.channels[0]
left = pca.channels[1]
left.duty_cycle = 32767
right.duty_cycle = 32767

print("Ready!")
time.sleep(15)

right.duty_cycle = 42765
left.duty_cycle = 22765

time.sleep(6)

right.duty_cycle = 22765

time.sleep(10)

left.duty_cycle = 32767
right.duty_cycle = 32767
