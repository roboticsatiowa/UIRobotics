from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json
import webbrowser
from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.widgets import Slider, Button
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QLabel, QMainWindow, QApplication, QGridLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800,800,1600,800)
        self.setWindowTitle("PyQt5 Slider")
        self.setWindowIcon(QIcon("python.png"))
        self.hbox = QHBoxLayout()
        # self.gps = QWidget(self)
        self.left = 1000
        self.top = 1000
        self.width = 640
        self.height = 480
        # self.resize(self.width(), self.height())

        # self.GPS()
        #layout = QVBoxLayout()
        theSlider = sliderdemo(self)
        self.setCentralWidget(theSlider)
        #layout.addWidget(theSlider)
        theGPS = gps(self)
        # self.setCentralWidget(theGPS)
        #layout.addWidget(theGPS)




class sliderdemo(QWidget):
   def __init__(self, parent):
      super(sliderdemo, self).__init__(parent)

      layout = QVBoxLayout()
      self.l1 = QLabel("Zoom")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)

      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(0)
      self.sl.setMaximum(24)
      self.sl.setValue(12)
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(1)

      layout.addWidget(self.sl)
      self.sl.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("GPS slider")

      self.label = QLabel("12", self)

   def valuechange(self):
      size = self.sl.value()
      self.label.setText(str(self.sl.value()))


class gps(QWidget):
        zm = 12

    # Checks to see if user input is valid (-90 - 90)
        def ifValidLatitude(x):
            try:
                x = float(x)
            except:
                if not isinstance(x, float):
                    print("Invalid input")
                    return False
            if x > 90 or x < -90:
                print("Invalid input")
                return False
            return True

        # Checks to see if the user input is valid ( -180 - 180)
        def ifValidLongitude(x):
            try:
                x = float(x)
            except:
                if not isinstance(x, float):
                    print("Invalid input")
                    return False
            if x > 180 or x < -180:
                print("Invalid input")
                return False
            return True
        # 10/07/2021 Charlie - taking input GPS coordinates and only accepting floats

        lat = input("Enter latitude: ")
        while not ifValidLatitude(lat):
            lat = input("Enter latitude: ")

        lng = input("Enter longitude: ")
        while not ifValidLongitude(lng):
            lng = input("Enter longitude: ")
        # 10/10/2021 Charlie - finished taking in GPS coordinates with valid inputs

        def getMapImage(lat, lng, zoom = zm):
            urlbase = "http://maps.google.com/maps/api/staticmap?"
            GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
            args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
            args = args + "&key=" + GOOGLEAPIKEY
            mapURL = urlbase+args
            urlretrieve(mapURL, 'googlemap.png')
            # img = Image.open('googlemap.png')
            # img.show()
            label = QLabel(self)
            pixmap = QPixmap('googlemap.png')
            label.setPixmap(pixmap)
            # self.resize(pixmap.width(), pixmap.height())

# def main():
#    app = QApplication(sys.argv)
#    ex = sliderdemo()
#    ex.show()
#    sys.exit(app.exec_())
#
# if __name__ == '__main__':
#    main()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    # ex = sliderdemo()
    # ex.show()
    win.show()

    sys.exit(app.exec_())
