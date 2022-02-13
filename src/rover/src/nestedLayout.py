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

    def _create_gps_buttons(self):
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

    def _create_silder(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(24)
        self.slider.setValue(12)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        # self.slider.setGeometry(700, 600, 200, 50)
        # self.slider.valueChanged.connect(self.sliderValueChanged)
        self.gps_button_slider_layout.addWidget(self.slider)

    def _create_gps(self):
        # label3 = QLabel("GPS", self)
        # label3.setStyleSheet("border: 3px solid orange")
        # label3.setFont(QFont('Times', 15))
        # label3.setAlignment(Qt.AlignCenter)

        self.label3 = QLabel("GPS", self)
        # self.label3.setGeometry(700, 400, 200,200)
        # GPSpixmap = QPixmap('googlemap.png')
        #label3.setPixmap(GPSpixmap)
        self.label3.setStyleSheet("border: 3px solid orange")
        self.label3.setFont(QFont('Times', 15))
        self.label3.setAlignment(Qt.AlignCenter)
        self.gps_layout.addWidget(self.label3)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
