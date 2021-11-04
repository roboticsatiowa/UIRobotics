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
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow, QApplication, QGridLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class gps(QMainWindow):
        zm = 12
        lat = 0
        lng = 0

        def __init__(self):
            super(gps, self).__init__()
            hbox = QHBoxLayout(self)
            gps.getMapImage(self, self.lat, self.lng, self.zm)
            # QLabel
            label = QLabel(self)
            pixmap = QPixmap('googlemap.png')
            pixmap = pixmap.scaled(700, 800, Qt.KeepAspectRatio, Qt.FastTransformation)
            label.setPixmap(pixmap)
            hbox.addWidget(label)
            self.setLayout(hbox)

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


        # 10/10/2021 Charlie - finished taking in GPS coordinates with valid inputs

        def getMapImage(self, lat, lng, zoom):
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
            self.resize(pixmap.width(), pixmap.height())
            self.move(300,300)
            label.setPixmap(pixmap)

            # pixmap = pixmap.scaled(700, 800, Qt.KeepAspectRatio, Qt.FastTransformation)
        lat = input("Enter latitude: ")
        while not ifValidLatitude(lat):
            lat = input("Enter latitude: ")

        lng = input("Enter longitude: ")
        while not ifValidLongitude(lng):
            lng = input("Enter longitude: ")




def main():
   app = QApplication(sys.argv)
   ex = gps()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
