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
        self.top_layout = QHBoxLayout()
        #nest layouts
        self.main_layout.addLayout(self.top_layout)



        self.gps_layout = QVBoxLayout()

        self.gps_button_slider_layout = QGridLayout() # add to gps_layout

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        self.main_layout.addLayout(self.gps_layout)

        self._create_buttons()
        self._create_video_feeds()
        
    def _create_video_feeds(self):
        self.vid1 = QLabel(self) #realsense
        self.vid2 = QLabel(self)
        self.vid1.setStyleSheet("border: 3px solid orange")
        self.vid2.setStyleSheet("border: 3px solid orange")
        self.top_layout.addWidget(self.vid1)
        self.top_layout.addWidget(self.vid2)

    def _create_buttons(self):
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
        self.gps_layout.addLayout(self.gps_button_slider_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
