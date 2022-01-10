import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

pca.frequency = 1000
led_channel = pca.channels[1]
led_channel_2 = pca.channels[0]
#led_channel.duty_cycle = 0
#time.sleep(2)

#led_channel.duty_cycle = 65535
#time.sleep(2)

led_channel.duty_cycle = 32765
led_channel_2.duty_cycle = 32765
