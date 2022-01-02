#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QStatusBar, QToolBar
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

from functools import partial
import cv2
import numpy as np

import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.pub_mode = rospy.Publisher('mode', String, queue_size=10)
        rospy.Subscriber('/camera/color/image_raw/compressed', CompressedImage, self._camera_color_callback)

        self.setWindowTitle('Robotics at Iowa GUI')
        self.setFixedSize(1000, 500)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createButtons()

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {'AUTO': (0, 0),
                   'TELEOP': (0,1)
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(150, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def _camera_color_callback(self, data):
        np_frame = np.fromstring(data.data, np.uint8)
        self.frame = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)

    def sendAuto(self):
        msg="AUTO"
        if not rospy.is_shutdown():
            self.pub_mode.publish(msg)

    def sendTeleop(self):
        msg="TELEOP"
        if not rospy.is_shutdown():
            self.pub_mode.publish(msg)

class Ctrl:
    """Controller class."""
    def __init__(self, win):
        """Controller initializer."""
        self._win = win
        self._connectSignals()

    def _connectSignals(self):
        """Connect signals and slots."""
        self._win.buttons['AUTO'].clicked.connect(self._win.sendAuto)
        self._win.buttons['TELEOP'].clicked.connect(self._win.sendTeleop)


if __name__ == '__main__':
    try:
        # pub_mode=rospy.Publisher('mode', String, queue_size=10)
        rospy.init_node('gui')
        # rate = rospy.Rate(10) # currently not used

        app = QApplication(sys.argv)
        win = Window()
        win.show()
        Ctrl(win=win)
        sys.exit(app.exec_())
    except rospy.ROSInterruptException:
        pass
