# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
from urllib.request import urlopen, urlretrieve
import sys

#commit comment
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.window_w = 1000
        self.window_h = 800

        # creating layouts
        self.main_layout = QVBoxLayout()
        self.gps_layout = QVBoxLayout()
        self.gps_button_slider_layout = QFormLayout() # add to gps_layout
        print("test")

    def _create_buttons():
        self.buttons = {}
        buttons = {'LAT': (0, 0), 'LNG': (0,1)}

        # create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            # create button
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(150, 40)

            # connect button to publisher (currenly just publishes button text)
            self.buttons[btnText].clicked.connect(lambda state, msg=btnText: self._send_mode(msg))

            # add button to button layout
            self.gps_button_slider_layout.addWidget(self.buttons[btnText], pos[0], pos[1])
            self.gps_layout.addLayout(gps_button_slider_layout)


if __name__ == '__main__':
    print("test")
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
