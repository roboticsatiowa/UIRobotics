from matplotlib.widgets import Slider, Button
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow, QApplication, QGridLayout, QVBoxLayout)
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow, QApplication, QGridLayout, QVBoxLayout, QScrollArea)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
# from ui_stackedWidget import Ui_StackedWidget
@ -21,36 +21,36 @@ class Window(QWidget):
        self.setGeometry(800,800,1600,800)
        self.setWindowTitle("PyQt5 Slider")
        self.setWindowIcon(QIcon("python.png"))
        self.hbox = QHBoxLayout()
        layout = QVBoxLayout()
        self.layout = QVBoxLayout()
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.setLayout(self.layout)
        # self.gps = QWidget(self)
        self.left = 1000
        self.top = 1000
        self.width = 640
        self.height = 480

        # self.stackedWidget = QtWidgets.QStackedWidget()
        # self.ui = Ui_StackedWidget()
        # self.ui.setupUi(self.stackedWidget)
        # self.setCentralWidget(self.stackedWidget)
        self.container = QWidget()
        self.gridLayout = QGridLayout(self.container)
        self.scrollArea.setWidget(self.container)
        self.layout.addWidget(self.scrollArea)

        # self.resize(self.width(), self.height())

        gps = GPS()
        #layout = QVBoxLayout()

        theSlider = sliderdemo(self)
        self.addWidget(gps)
        self.addWidget(theSlider)
        #layout.addWidget(theSlider)
        #layout.addWidget(theGPS)
        self.gps = GPS()
        self.slider = sliderdemo()
        self.layout.addWidget(self.gps)
        self.layout.addWidget(self.slider)





class sliderdemo(QWidget):
   def __init__(self, parent):
      super(sliderdemo, self).__init__(parent)
   def __init__(self):
      super(sliderdemo, self).__init__()

      layout = QVBoxLayout()
      self.l1 = QLabel("Zoom")
@ -93,7 +93,8 @@ class GPS(QWidget):
        while not GPS.ifValidLongitude(lng):
            lng = input("Enter longitude: ")

        zm = 3
        zm = sliderdemo.self.sl.value()


        pixmap = QPixmap(GPS.getMapImage(self, lat, lng, zm))
