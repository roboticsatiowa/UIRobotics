#!/usr/bin/env python3

import sys
from functools import partial
import cv2
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

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
        # self.pub_mode = rospy.Publisher('mode', String, queue_size=10)
        # rospy.Subscriber('/realsense_camera_0/color/image_raw/compressed', CompressedImage, self._realsense_camera_callback)
        rospy.Subscriber('/usb_camera_0/image_raw/compressed', CompressedImage, self._usb_camera_callback_0)
        rospy.Subscriber('/usb_camera_1/image_raw/compressed', CompressedImage, self._usb_camera_callback_1)

        # create window
        self.setWindowTitle('Robotics at Iowa GUI')
        self.setFixedSize(self.window_w, self.window_h)

        # create general layout
        # TODO: why is central widget necessary?
        # self.general_layout = QVBoxLayout()
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        # self.bottom_layout = QHBoxLayout()
        # self.bottom_left_layout = QVBoxLayout()
        # self.bottom_middle_layout = QVBoxLayout()
        # self.timer_button_layout = QGridLayout()
        # self.bottom_right_layout = QVBoxLayout()
        # self.gps_layout = QVBoxLayout()
        # self.lat_lng_layout = QHBoxLayout()

        self.main_layout.addLayout(self.top_layout)
        # self.main_layout.addLayout(self.bottom_layout)
        # self.bottom_layout.addLayout(self.bottom_left_layout)
        # self.bottom_layout.addLayout(self.bottom_middle_layout)
        # self.bottom_layout.addLayout(self.bottom_right_layout)
        # self.bottom_right_layout.addLayout(self.gps_layout)
        # self.bottom_right_layout.addLayout(self.lat_lng_layout)


        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # create gui within layout
        # self._create_modes()
        self._create_video_feeds()
        # self._create_timer()
        # self._create_timer_buttons()

    # def _create_modes(self):
    #     self.stopButton = QPushButton("STOP ROVER", self)
    #     self.stopButton.clicked.connect(lambda state, msg="STOP": self._send_mode(msg))

    #     # creating auto mode button
    #     self.autoButton = QPushButton("AUTO MODE", self)
    #     self.autoButton.clicked.connect(lambda state, msg="AUTO": self._send_mode(msg))

    #     # creating manual mode button
    #     self.manualButton = QPushButton("MANUAL MODE", self)
    #     self.manualButton.clicked.connect(lambda state, msg="MANUAL": self._send_mode(msg))

    #     #adding buttons to layout
    #     self.bottom_left_layout.addWidget(self.stopButton)
    #     self.bottom_left_layout.addWidget(self.autoButton)
    #     self.bottom_left_layout.addWidget(self.manualButton)


    def _create_video_feeds(self):
        # create two video feeds
        self.vid1 = QLabel(self)
        self.vid2 = QLabel(self)

        self.top_layout.addWidget(self.vid1)
        self.top_layout.addWidget(self.vid2)

    # def _create_timer(self):
    #     self.label = QLabel("//TIMER//", self)
    #     self.label.setStyleSheet("border : 3px solid black")
    #     self.label.setFont(QFont('Times', 15))
    #     self.bottom_middle_layout.addWidget(self.label)
    #     self.bottom_middle_layout.addLayout(self.timer_button_layout)

    # def _create_timer_buttons(self):
    #      # creating push button to get time in seconds
    #      self.button = QPushButton("Set time", self)
    #      self.button.clicked.connect(self.get_seconds)
    #      #self.button.clicked.connect(self.get_seconds)
    #      # creating start button
    #      self.start_button = QPushButton("Start", self)
    #      self.start_button.clicked.connect(self.start_action)
    #      #self.start_button.clicked.connect(self.start_action)
    #      # creating pause button
    #      self.pause_button = QPushButton("Pause", self)
    #      self.pause_button.clicked.connect(self.pause_action)
    #      #self.pause_button.clicked.connect(self.pause_action)
    #      # creating reset button
    #      self.reset_button = QPushButton("Reset", self)
    #      self.reset_button.clicked.connect(self.reset_action)
    #      #self.reset_button.clicked.connect(self.reset_action)
    #      self.timer_button_layout.addWidget((self.button), 0,0)
    #      self.timer_button_layout.addWidget((self.start_button), 0,1)
    #      self.timer_button_layout.addWidget((self.pause_button), 1,0)
    #      self.timer_button_layout.addWidget((self.reset_button), 1,1)

    # def reset_action(self):
	# 	# making flag false
    #     self.start = False

	# 	# setting count value to 0
    #     self.count = 0

	# 	# setting label text
    #     self.label.setText("//TIMER//")

    # def get_seconds(self):

	# 	# making flag false
    #     self.start = False

	# 	# getting seconds and flag
    #     second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

	# 	# if flag is true
    #     if done:
	# 		# changing the value of count
    #         self.count = second * 10

	# 		# setting text to the label

    #         self.label.setText(str(second))

    # def start_action(self):
	# 	# making flag true
    #     self.start = True

	# 	# count = 0
    #     if self.count == 0:
    #         self.start = False
    # def pause_action(self):

	# 	# making flag false
    #     self.start = False

    # def reset_action(self):

	# 	# making flag false
    #     self.start = False

	# 	# setting count value to 0
    #     self.count = 0

	# 	# setting label text
    #     self.label.setText("//TIMER//")

#    def _realsense_camera_callback(self, data):
#        pixmap = self._compressed_image_to_pixmap(data.data, width_scale=self.window_w//2)
#        self.vid1.setPixmap(pixmap)

    def _usb_camera_callback_0(self, data):
        pixmap = self._compressed_image_to_pixmap(data.data, width_scale=self.window_w//2)
        self.vid1.setPixmap(pixmap)

    def _usb_camera_callback_1(self, data):
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

    # def _send_mode(self, msg):
    #     # publish mode from button
    #     if not rospy.is_shutdown():
    #         self.pub_mode.publish(msg)


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
