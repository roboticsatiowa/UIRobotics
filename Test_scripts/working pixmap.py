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
        self.pixmap = QPixmap(App.getMapImage(41.6, -91.5, self.theSlider.sl.value()))
        self.image = QLabel(self.widget)
        self.image.setPixmap(self.pixmap)
        self.image.setFixedSize(self.pixmap.size())
        self.theSlider.sl.valueChanged.connect(self.refresh)
        
        p = self.geometry().bottomRight() - self.image.geometry().bottomRight() - QPoint(100, 100)
        self.image.move(p)
        
        
    def refresh(self):
    
        self.image.clear()
        self.pixmap = QPixmap('googlemap.png')
        # self.image2 = QLabel(self.widget)
        self.image.setPixmap(self.pixmap)
        #self.image2.setFixedSize(self.pixmap2.size())
        #self.theSlider.sl.valueChanged.connect(self.image2.clear)
    
#gps image code        
class App(QWidget):

    def __init__(self):
        super().__init__()
        #self.title = 'PyQt5 image - pythonspot.com'
        #self.left = 10
        #self.top = 10
        #self.width = 640
        #self.height = 480
        #self.initUI()
    def getMapImage(lat, lng, zoom):
            urlbase = "http://maps.google.com/maps/api/staticmap?"
            GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
            args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
            args = args + "&key=" + GOOGLEAPIKEY
            mapURL = urlbase+args
            urlretrieve(mapURL, 'googlemap.png')
            img = QPixmap('googlemap.png')
            return img
        
     
#slider code
class sliderdemo(QWidget):
   def __init__(self, parent):
      super(sliderdemo, self).__init__(parent)

      layout = QVBoxLayout()
      self.l1 = QLabel("Zoom")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(1)
      self.sl.setMaximum(24)
      self.sl.setValue(12)
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(1)
      
      layout.addWidget(self.sl)
      self.sl.valueChanged.connect(self.valuechange)
      self.setLayout(layout)

      self.label = QLabel("12", self)

   def valuechange(self):
      self.label.setText(str(self.sl.value()))
      App.getMapImage(41.6, -91.5, self.sl.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensize = app.desktop().availableGeometry().size()

    ex = ExampleWindow(screensize)
    ex.show()

sys.exit(app.exec_())
