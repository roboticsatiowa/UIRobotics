#!/usr/bin/env python3

import sys
import time
import datetime
from functools import partial
import cv2
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage, Image
from urllib.request import urlopen, urlretrieve


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
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        self.bottom_left_layout = QVBoxLayout()
        self.bottom_middle_layout = QVBoxLayout()
        self.timer_button_layout = QGridLayout()
        self.bottom_right_layout = QVBoxLayout()
        self.gps_layout = QVBoxLayout()
        self.lat_lng_layout = QHBoxLayout()
        self.bottom_right_widget = QWidget()
        self.bottom_right_widget.setLayout(self.bottom_right_layout)
        self.bottom_right_widget.setFixedWidth(480)
        self.bottom_layout.addWidget(self.bottom_right_widget)
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        self.bottom_layout.addLayout(self.bottom_left_layout)
        self.bottom_layout.addLayout(self.bottom_middle_layout)
        self.bottom_layout.addLayout(self.bottom_right_layout)
        self.bottom_right_layout.addLayout(self.gps_layout)
        self.bottom_right_layout.addLayout(self.lat_lng_layout)
        self.bottom_middle_layout.addLayout(self.timer_button_layout)

        # self.bottom_right_layout.setStretch(2,-2)




        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # create gui within layout
        self._create_modes()
        self._create_video_feeds()
        self._create_timer_components()
        self._create_gps_buttons()
        self._create_gps()
        self._create_slider()


    def _create_modes(self):
        self.stopButton = QPushButton("STOP ROVER", self)
        self.stopButton.clicked.connect(lambda state, msg="STOP": self._send_mode(msg))

        # creating auto mode button
        self.autoButton = QPushButton("AUTO MODE", self)
        self.autoButton.clicked.connect(lambda state, msg="AUTO": self._send_mode(msg))

        # creating manual mode button
        self.manualButton = QPushButton("MANUAL MODE", self)
        self.manualButton.clicked.connect(lambda state, msg="MANUAL": self._send_mode(msg))

        #adding buttons to layout
        self.bottom_left_layout.addWidget(self.stopButton)
        self.bottom_left_layout.addWidget(self.autoButton)
        self.bottom_left_layout.addWidget(self.manualButton)

    def _create_gps_buttons(self):
        #creating latitude input text box
        latitudeButton = QPushButton("Set Latitude", self)
        latitudeButton.clicked.connect(self._get_latitude)
        latitudeButton.setFont(QFont('Times', 11))

        #creating longitude input text box
        longitudeButton = QPushButton("Set Longitude", self)
        longitudeButton.clicked.connect(self._get_longitude)
        longitudeButton.setFont(QFont('Times', 11))

        self.lat_lng_layout.addWidget(latitudeButton)
        self.lat_lng_layout.addWidget(longitudeButton)

    def _create_slider(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(1)
        self.slider.setMaximum(24)
        self.slider.setValue(12)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setGeometry(400, 30, 800, 1000)
        self.slider.valueChanged.connect(self._slider_value_changed)
        self.bottom_right_layout.addWidget(self.slider)

    def _create_gps(self):

        self.label3 = QLabel("GPS", self)
        self.label3.setStyleSheet("border: 3px solid orange")
        self.label3.setFont(QFont('Times', 15))
        self.label3.setAlignment(Qt.AlignCenter)
        self.gps_layout.addWidget(self.label3)


    def _get_map_image(self, lat, lng, zoom):
        urlbase = "http://maps.google.com/maps/api/staticmap?"
        GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
        args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
        args = args + "&key=" + GOOGLEAPIKEY
        mapURL = urlbase+args
        urlretrieve(mapURL, 'googlemap.png')
        img = QPixmap('googlemap.png')
        return img

    def _get_latitude(self):
        self.latitude, ok = QInputDialog.getDouble(self, "Latitude", "Enter Latitude", 0, -90, 90)
    #method to get longitude
    def _get_longitude(self):
        self.longitude, ok = QInputDialog.getDouble(self, "Longitude", "Enter Longitude", 0, -180, 180)

    #slider value change method
    def _slider_value_changed(self):
        self._get_map_image(self.latitude, self.longitude, self.slider.value())
        self.label3.clear()
        GPSpixmap = QPixmap('googlemap.png')
        self.label3.setPixmap(GPSpixmap)


    def _create_video_feeds(self):
        # create two video feeds
        self.vid1 = QLabel(self)
        self.vid2 = QLabel(self)

        self.top_layout.addWidget(self.vid1)
        self.top_layout.addWidget(self.vid2)

    def _create_timer_components(self):
        self.count = 0
        self.start = False
        button = QPushButton("Set Time", self)
        button.clicked.connect(self.get_seconds)

        self.label = QLabel("//TIMER//", self)
        self.bottom_layout.addWidget(self.label)

        start_button = QPushButton("Start", self)
        start_button.clicked.connect(self.start_action)
        pause_button = QPushButton("Pause", self)
        pause_button.clicked.connect(self.pause_action)
        reset_button = QPushButton("Reset", self)
        reset_button.clicked.connect(self.reset_action)

        self.timer_button_layout.addWidget(self.label)
        self.timer_button_layout.addWidget(button)
        self.timer_button_layout.addWidget(start_button)
        self.timer_button_layout.addWidget(pause_button)
        self.timer_button_layout.addWidget(reset_button)
        timer = QTimer(self)
        timer.timeout.connect(self._show_time)
        timer.start(100)

    def _show_time(self):
        if self.start:
            self.count -= 1
            if self.count == 0:
                self.start = False
                self.label.setText("Completed")
        if self.start:
            text = str(self.count / 10) + " s"

            self.label.setText(text)

    def get_seconds(self):
        self.start = False
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

        if done:
            self.count = second * 10

            self.label.setText(str(second))

    def start_action(self):
        self.start = True
        if self.count == 0:
            self.start = False

    def pause_action(self):
        self.start = False

    def reset_action(self):
        self.start = False

        self.count = 0;
        self.label.setText("//TIMER//")

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
