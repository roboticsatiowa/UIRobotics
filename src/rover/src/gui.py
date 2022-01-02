#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QStatusBar, QToolBar
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage

from functools import partial
import cv2
import numpy as np

import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # initialize
        self.window_w = 1000
        self.window_h = 500

        # ros pub and subs
        self.pub_mode = rospy.Publisher('mode', String, queue_size=10)
        rospy.Subscriber('/camera/color/image_raw/compressed', CompressedImage, self._camera_color_callback)

        # create window
        self.setWindowTitle('Robotics at Iowa GUI')
        self.setFixedSize(self.window_w, self.window_h)

        # create general layout
        # TODO: make cleaner
        self.general_layout = QVBoxLayout()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.general_layout)

        # create gui within layout
        self._create_video_feed()
        self._create_buttons()

    def _create_buttons(self):
        # buttons dict
        self.buttons = {}
        buttons = {'AUTO': (0, 0), 'TELEOP': (0,1)}

        # create the buttons and add them to the grid layout
        buttons_layout = QGridLayout()
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(150, 40)
            buttons_layout.addWidget(self.buttons[btnText], pos[0], pos[1])

        # add buttons layout to the general layout
        self.general_layout.addLayout(buttons_layout)

    def _create_video_feed(self):
        self.vid = QLabel(self)
        self.general_layout.addWidget(self.vid)

    def _camera_color_callback(self, data):
        # convert image: compressed string --> np --> cv2 --> pyqt
        np_img = np.fromstring(data.data, np.uint8)
        bgr_img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        rgb_image = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        qt_img = qt_img.scaledToWidth(self.window_w//2)

        # place image on gui
        pixmap = QPixmap(QPixmap.fromImage(qt_img))
        self.vid.setPixmap(pixmap)

    def send_auto(self):
        msg = "AUTO"
        if not rospy.is_shutdown():
            self.pub_mode.publish(msg)

    def send_teleop(self):
        msg = "TELEOP"
        if not rospy.is_shutdown():
            self.pub_mode.publish(msg)

class Ctrl:
    def __init__(self, win):
        self._win = win
        self._connect_signals()

    def _connect_signals(self):
        self._win.buttons['AUTO'].clicked.connect(self._win.send_auto)
        self._win.buttons['TELEOP'].clicked.connect(self._win.send_teleop)


if __name__ == '__main__':
    try:
        # initialize ros node
        rospy.init_node('gui')
        # rate = rospy.Rate(10)

        # create gui
        app = QApplication(sys.argv)
        win = Window()
        win.show()
        Ctrl(win)
        sys.exit(app.exec_())
    except rospy.ROSInterruptException:
        pass
