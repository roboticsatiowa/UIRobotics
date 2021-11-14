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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from ui_stackedWidget import Ui_StackedWidget

class ExampleWindow(QMainWindow):
    def __init__(self, windowsize):
        super().__init__()
        self.windowsize = windowsize
        self.initUI()
    def initUI(self):
        self.setFixedSize(self.windowsize)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        #create widget
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        #add slider widget
        self.theSlider = sliderdemo(self)
        
        layout_box = QHBoxLayout(self.widget)
        layout_box.setContentsMargins(0, 0, 0, 0)
        layout_box.addWidget(self.theSlider)
        #add pixmap widget
        self.pixmap2 = QPixmap(App.getMapImage(41.6, -91.5, self.theSlider.sl.value()))
        self.image2 = QLabel(self.widget)
        self.image2.setPixmap(self.pixmap2)
        self.image2.setFixedSize(self.pixmap2.size())
        self.theSlider.sl.valueChanged.connect(self.refresh)
        
        p = self.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        self.image2.move(p)
        
        
    def refresh(self):
    
        self.image2.clear()
        self.pixmap2 = QPixmap('googlemap.png')
        # self.image2 = QLabel(self.widget)
        self.image2.setPixmap(self.pixmap2)
        #self.image2.setFixedSize(self.pixmap2.size())
        #self.theSlider.sl.valueChanged.connect(self.image2.clear)


class sliderdemo(QWidget):
   def __init__(self):
      super(sliderdemo, self).__init__()

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


class GPS(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        hbox = QHBoxLayout(self)
        # lat = input("Enter latitude: ")
        lat = input("Enter latitude: ")
        while not GPS.ifValidLatitude(lat):
            lat = input("Enter latitude: ")

        lng = input("Enter longitude: ")
        while not GPS.ifValidLongitude(lng):
            lng = input("Enter longitude: ")

        zm = sliderdemo.self.sl.value()
        

        pixmap = QPixmap(GPS.getMapImage(self, lat, lng, zm))

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Image with PyQt')
        pixmap = pixmap.scaled(700, 800, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.show()

    def getMapImage(self, lat, lng, zoom):
        urlbase = "http://maps.google.com/maps/api/staticmap?"
        GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
        args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
        args = args + "&key=" + GOOGLEAPIKEY
        mapURL = urlbase+args
        urlretrieve(mapURL, 'googlemap.png')
        img = QPixmap('googlemap.png')


        return img
        # img = Image.open('googlemap.png')
        # img.show()
        # label = QLabel(self)
        # pixmap = QPixmap('googlemap.png')
        # self.resize(pixmap.width(), pixmap.height())
        # # self.move(300,300)
        # label.setPixmap(pixmap)

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

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(400, 300)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(130, 80, 111, 51))
        self.label.setObjectName("label")
        StackedWidget.addDockWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(90, 160, 161, 91))
        self.label_2.setObjectName("label_2")
        StackedWidget.addDockWidget(self.page_2)
        StackedWidget

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.label.setText(_translate("StackedWidget", "first page"))
        self.label_2.setText(_translate("StackedWidget", "2nd page"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    # ex = sliderdemo()
    # ex.show()
    win.show()

    sys.exit(app.exec_())
