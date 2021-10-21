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
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QLabel, QMainWindow, QApplication, QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

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

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,200)
        self.setWindowTitle("PyQt5 Slider")
        self.setWindowIcon(QIcon("python.png"))
        hbox = QHBoxLayout()

        self.slider = QSlider(self)
        self.gps = QWidget(self)

        # self.GPS(self)
        # self.slider(self)

    def slider(self):

        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setValue(12)
        self.slider.setMaximum(24)
        self.slider.valueChanged.connect(self.changed_slider)
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

    def GPS(self):
        self.title = "GUI"
        self.setWindowTitle(self.title)
        label = QLabel(self)
        getMapImage(lat, lng, zm)
        img = Image.open('googlemap.png')
        image = ImageQt(img)
        pixmap = QPixmap.fromImage(image)

        self.label = QLabel("")
        # self.im = QPixmap(pixmap)
        # self.label.setPixmap(self.im)
        #
        # self.grid = QGridLayout()
        # self.grid.addWidget(self.label,1,1)
        # self.setLayout(self.grid)

        #window requrements like geometry,icon and title



        # self.label = QLabel("")
        #self.label.setFont(QFont("Comic Sans", 15))




        img = Image.open('googlemap.png')
        image = ImageQt(img)
        pixmap = QPixmap.fromImage(image)

        self.im = QPixmap(pixmap)
        self.label.setPixmap(self.im)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label,1,1)
        self.setLayout(self.grid)

        self.setGeometry(50,50,320,200)
        self.setWindowTitle("PyQT show image")


    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))
        zm = self.slider.value()




    # img = Image.open('googlemap.png')
    # img.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # Ctrl(win=win)
    sys.exit(app.exec_())
