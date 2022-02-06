#!/usr/bin/env python3

import sys
from functools import partial
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QSlider, QWidget, QLabel, QPushButton, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QFont
from urllib.request import urlopen, urlretrieve
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage, Image


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # initialize
        self.window_w = 1000
        self.window_h = 800

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


        # create slider


        # create gui within layout
        self._create_video_feeds()
        self._create_buttons()
        # self._create_silder()
        # self.UiComponents()

    # def _create_silder(self):
    #     self.slider = QSlider(Qt.Horizontal, self)
    #     self.slider.setMinimum(1)
    #     self.slider.setMaximum(24)
    #     self.slider.setValue(12)
    #     self.slider.setTickPosition(QSlider.TicksBelow)
    #     self.slider.setTickInterval(1)
    #     self.slider.setGeometry(700, 600, 200, 50)
    #     self.slider.valueChanged.connect(self.sliderValueChanged)
    #
    #     slider_layout = QHBoxLayout()
    #     slider_layout.addWidget(self.slider)
    #
    #     self.general_layout.addLayout(slider_layout)

# method for widgets
    # def UiComponents(self):
    #
    # 	# variables
    # 	# count variable
    #     self.count = 0
    #     self.latitude = 41.6
    #     self.longitude = -91.5
    #
    # 	# start flag
    #     self.start = False

       #  creating label as camera feed placeholder
       # pic = QLabel(self)
       # pixmap = QPixmap("rover1.png")
       # smaller_pixmap = pixmap.scaled(400, 300, Qt.KeepAspectRatio, Qt.FastTransformation)
       # pic.setPixmap(smaller_pixmap)
       # pic.resize(400,300)
       # pic.move(50,50)
       # pic.show()
       #
       # pic1 = QLabel(self)
       # pixmap2 = QPixmap("astronaut.png")
       # smaller_pixmap2 = pixmap2.scaled(400,300, Qt.KeepAspectRatio, Qt.FastTransformation)
       # pic1.setPixmap(smaller_pixmap2)
       # pic1.resize(400,300)
       # pic1.move(550,50)
       # pic1.show()

        # label1 = QLabel(self)
        # label1.setGeometry(50, 50,400,300)
        # label1.setStyleSheet("border: 3px solid orange")
        # label1.setFont(QFont('Times', 15))
        # label1.setAlignment(Qt.AlignCenter)
        #
        # label2 = QLabel(self)
        # label2.setGeometry(550, 50, 400, 300)
        # label2.setStyleSheet("border: 3px solid orange")
        # label2.setFont(QFont('Times', 15))
        # label2.setAlignment(Qt.AlignCenter)

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
        self.vid1 = QLabel(self) #realsense
        self.vid2 = QLabel(self)
        # self.vid2.setGeometry(50, 50,400,300) #usb camera
        # self.vid1.setGeometry(50, 50,400,300)

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



    # def sliderValueChanged(self):
    #     self.getMapImage(self.latitude, self.longitude, self.slider.value())
    #     self.label3.clear()
    #     GPSpixmap = QPixmap('googlemap.png')
    #     self.label3.setPixmap(GPSpixmap)
    #
    # def getMapImage(self, lat, lng, zoom):
    #     urlbase = "http://maps.google.com/maps/api/staticmap?"
    #     GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
    #     args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
    #     args = args + "&key=" + GOOGLEAPIKEY
    #     mapURL = urlbase+args
    #     urlretrieve(mapURL, 'googlemap.png')
    #     img = QPixmap('googlemap.png')
    #     return img

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
