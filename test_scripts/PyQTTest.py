from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
WIDTH = 500
HEIGHT = 300

def buttonPress():
    print("Sending GPS Coordinates...")

    
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,WIDTH,HEIGHT)
win.setWindowTitle("CodersLegacy")
 
button = QtWidgets.QPushButton(win)
button.clicked.connect(buttonPress)
button.setText("A Button")
button.move(WIDTH/2,HEIGHT/2)
win.show()
sys.exit(app.exec_())
