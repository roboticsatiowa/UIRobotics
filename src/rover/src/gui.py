#!/usr/bin/env python3

import sys
from functools import partial
import cv2
import numpy as np

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage, Image


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # initialize
        self.window_w = 1000
        self.window_h = 500

        # ros pub and subs
        self.pub_mode = rospy.Publisher('mode', String, queue_size=10)
        rospy.Subscriber('/realsense_camera_0/color/image_raw/compressed', CompressedImage, self._realsense_camera_callback)
        rospy.Subscriber('/usb_camera_0/image_raw/compressed', CompressedImage, self._usb_camera_callback)

        # create window
        self.setWindowTitle('Robotics at Iowa GUI')
        self.setFixedSize(self.window_w, self.window_h)

        # create general layout
        # TODO: why is central widget necessary?
        self.general_layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.general_layout)
        self.setCentralWidget(self.central_widget)

        # create gui within layout
        self._create_video_feeds()
        self._create_buttons()

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # map zoom/slider
    def valuechange(slider, self):
        sliderLabel = QLabel()
        sliderLabel.setGeometry(700, 650, 10, 10)
        sliderLabel.setStyleSheet("border: 3px solid orange")
        sliderLabel.setFont(QFont('Times', 15))
        sliderLabel.setAlignment(Qt.AlignCenter)

    # TODO: finish getMapImage
    # def getMapImage(self, lat, lng, zoom):
    #    urlbase = "http://maps.google.com/maps/api/staticmap?"
    #    GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"

    def UiComponents(self):

        # variables
        # count variables
        self.count = 0

        # start flag
        self.start = False

        # GPS container
        label1 = QLabel("GPS", self)
        label1.setGeometry(700, 400, 200, 200)
        label1.setStyleSheet("border: 3px solid orange")
        label1.setFont(QFont('Times', 15))
        label1.setAlignment(Qt.AlignCenter)

        # push button for time in seconds
        button = QPushButton("Set Time", self)
        button.setGeometry(325, 530, 150, 50)
        button.clicked.connect(self.get_seconds)

        # label showing time elapsed
        self.label = QLabel("//TIMER//", self)
        self.label.setGeometry(340, 470, 300, 50)
        self.label.setStyleSheet("border: 3px solid black")
        self.label.setFont(QFont('Times', 15))
        self.label.setAlignment(Qt.AlignCenter)

        # timer start button
        start_button = QPushButton("Start", self)
        start_button.setGeometry(500, 530, 150, 50)
        start_button.clicked.connect(self.start_action)

        # timer pause button
        pause_button = QPushButton("Pause", self)
        pause_button.setGeometry(325, 600, 150, 50)
        pause_button.clicked.connect(self.pause_action)

        # timer reset button
        reset_button = QPushButton("Reset", self)
        reset_button.setGeometry(500, 600, 150, 30)
        reset_button.clicked.connect(self.reset_action)

        # timer object
        timer = QTimer(self)
        # adding action to timer
        timer.timeout.connect(self.showTime)
        # update timer every tenth of a second
        timer.start(100)

        # slider for map
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(1)
        slider.setMaximum(24)
        slider.setValue(12)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(1)
        slider.setGeometry(700,600,300,50)
        slider.valueChanged.connect(self.valuechange)

# do not touch code below!
# beginning of already-existing gui code
    def _create_buttons(self):
        # buttons dict
        self.buttons = {}
        buttons = {'AUTO': (0, 0), 'TELEOP': (0,1)}

        # create the buttons and add them to the grid layout
        buttons_layout = QGridLayout()
        for btnText, pos in buttons.items():
            # create button
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(150, 40)

            # connect button to publisher (currenly just publishes button text)
            self.buttons[btnText].clicked.connect(lambda state, msg=btnText: self._send_mode(msg))

            # add button to button layout
            buttons_layout.addWidget(self.buttons[btnText], pos[0], pos[1])

        # add buttons layout to the general layout
        self.general_layout.addLayout(buttons_layout)

    def _create_video_feeds(self):
        # create two video feeds
        self.vid1 = QLabel(self)
        self.vid2 = QLabel(self)

        vid_layout = QHBoxLayout()
        vid_layout.addWidget(self.vid1)
        vid_layout.addWidget(self.vid2)

        self.general_layout.addLayout(vid_layout)

    def _realsense_camera_callback(self, data):
        pixmap = self._compressed_image_to_pixmap(data.data, width_scale=self.window_w//2)
        self.vid1.setPixmap(pixmap)

    def _usb_camera_callback(self, data):
        pixmap = self._compressed_image_to_pixmap(data.data, width_scale=self.window_w//2)
        self.vid2.setPixmap(pixmap)

    def _compressed_image_to_pixmap(self, compressed_img, width_scale):
        # convert image: compressed string --> np --> cv2 --> pyqt
        np_img = np.fromstring(compressed_img, np.uint8)
        bgr_img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb_img.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb_img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        qt_img = qt_img.scaledToWidth(width_scale)

        pixmap = QPixmap.fromImage(qt_img)

        return pixmap

    def _send_mode(self, msg):
        # publish mode from button
        if not rospy.is_shutdown():
            self.pub_mode.publish(msg)


if __name__ == '__main__':
    try:
        # initialize ros node
        rospy.init_node('gui')

        # create gui
        app = QApplication(sys.argv)
        win = Window()
        win.show()

        sys.exit(app.exec_())
    except rospy.ROSInterruptException:
        pass
