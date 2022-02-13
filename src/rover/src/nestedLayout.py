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

        self.bottom_layout = QHBoxLayout()
        self.bottom_left_layout = QVBoxLayout()
        self.bottom_middle_layout = QVBoxLayout()
        self.timer_button_layout = QFormLayout()
        self.bottom_right_layout = QVBoxLayout()
        self.gps_layout = QVBoxLayout()
        self.lat_lng_layout = QHBoxLayout()
        

        #nest layouts
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        self.bottom_layout.addLayout(self.bottom_left_layout)
        self.bottom_layout.addLayout(self.bottom_middle_layout)
        self.bottom_layout.addLayout(self.bottom_right_layout)
        self.bottom_middle_layout.addLayout(self.timer_button_layout)
        self.bottom_right_layout.addLayout(self.gps_layout)
        self.bottom_right_layout.addLayout(self.lat_lng_layout)
    

         # add to gps_layout

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        self.main_layout.addLayout(self.gps_layout)

        self._create_slider()
        self._create_gps_buttons()
        self._create_video_feeds()
        self._create_gps()
        self._create_modes()
        self._create_timer()
        self._create_timer_buttons()

    def _create_video_feeds(self):
        self.vid1 = QLabel(self) #realsense
        self.vid2 = QLabel(self)
        self.vid1.setStyleSheet("border: 3px solid orange")
        self.vid2.setStyleSheet("border: 3px solid orange")
        self.top_layout.addWidget(self.vid1)
        self.top_layout.addWidget(self.vid2)
    def _create_mode_buttons(self):
        # creating start button
        self.start_button = QPushButton("Start", self)
        #self.start_button.setGeometry(500, 530, 150, 50)
        self.start_button.clicked.connect(self.start_action)
        # creating pause button
        self.pause_button = QPushButton("Pause", self)
        #self.pause_button.setGeometry(325, 600, 150, 50)
        self.pause_button.clicked.connect(self.pause_action)
        # creating reset button
        self.reset_button = QPushButton("Reset", self)
        #self.reset_button.setGeometry(500, 600, 150, 50)
        self.reset_button.clicked.connect(self.reset_action)

        self.bottom_left_layout.addWidget(self.start_button)
        self.bottom_left_layout.addWidget(self.pause_button)
        self.bottom_left_layout.addWidget(self.reset_button)
    def _create_timer(self):
        
        self.label = QLabel("//TIMER//", self)
        self.label.setStyleSheet("border : 3px solid black")
        self.label.setFont(QFont('Times', 15))
        self.bottom_middle_layout.addWidget(self.label)
    def _create_timer_buttons(self):
         # creating push button to get time in seconds
         self.button = QPushButton("Set time", self)
         #self.button.clicked.connect(self.get_seconds)
         # creating start button
         self.start_button = QPushButton("Start", self)
         #self.start_button.clicked.connect(self.start_action)
         # creating pause button
         self.pause_button = QPushButton("Pause", self)
         #self.pause_button.clicked.connect(self.pause_action)
         # creating reset button
         self.reset_button = QPushButton("Reset", self)
         #self.reset_button.clicked.connect(self.reset_action)
         self.timer_button_layout.addWidget(self.button)
         self.timer_button_layout.addWidget(self.start_button)
         self.timer_button_layout.addWidget(self.pause_button)
         self.timer_button_layout.addWidget(self.reset_button)
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
            self.lat_lng_layout.addWidget(self.buttons[btnText])

    def _create_slider(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(24)
        self.slider.setValue(12)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        # self.slider.setGeometry(700, 600, 200, 50)
        # self.slider.valueChanged.connect(self.sliderValueChanged)
        self.bottom_right_layout.addWidget(self.slider)

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
    def start_action(self):
		# making flag true
        self.start = True

		# count = 0
        if self.count == 0:
            self.start = False

    def pause_action(self):

		# making flag false
        self.start = False
    def reset_action(self):

		# making flag false
        self.start = False

		# setting count value to 0
        self.count = 0

		# setting label text
        self.label.setText("//TIMER//")

    def _create_modes(self):
        self.stopButton = QPushButton("STOP ROVER", self)

        # stopButton.clicked.connect(self.stop_action)

        # creating auto mode button
        self.autoButton = QPushButton("AUTO MODE", self)

        # autoButton.clicked.connect(self.auto_action)

        # creating manual mode button
        self.manualButton = QPushButton("MANUAL MODE", self)

        # manualButton.clicked.connect(self.manual_action)

        #adding buttons to layout
        self.bottom_left_layout.addWidget(self.stopButton)
        self.bottom_left_layout.addWidget(self.autoButton)
        self.bottom_left_layout.addWidget(self.manualButton)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
