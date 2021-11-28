import sys,tty,termios
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

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print("up")
                right.duty_cycle = 42765
                left.duty_cycle = 22765
        elif k=='\x1b[B':
                print("down")
                right.duty_cycle = 22765
                left.duty_cycle = 42765
        elif k=='\x1b[C':
                print("right")
                right.duty_cycle = 42765
                left.duty_cycle = 42765
        elif k=='\x1b[D':
                print("left")
                right.duty_cycle = 22765
                left.duty_cycle = 22765
        else:
                print("not an arrow key!")	
                left.duty_cycle = 32767
                right.duty_cycle = 32767

def main():
        for i in range(0,20):
                get()

if __name__=='__main__':
        main()
