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
    def refresh(self):
        pixmap2 = QPixmap('googlemap.png')
        self.image2 = QLabel(widget)
        self.image2.setPixmap(pixmap2)
        self.image2.setFixedSize(pixmap2.size())
    def initUI(self):
        self.setFixedSize(self.windowsize)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        widget = QWidget()
        self.setCentralWidget(widget)
        self.theSlider = sliderdemo(self)
        '''
        self.image = QLabel()
        self.image.setPixmap(pixmap1)
        '''
        layout_box = QHBoxLayout(widget)
        layout_box.setContentsMargins(0, 0, 0, 0)
        layout_box.addWidget(self.theSlider)
        pixmap2 = QPixmap('googlemap.png')
        self.image2 = QLabel(widget)
        self.image2.setPixmap(pixmap2)
        self.image2.setFixedSize(pixmap2.size())
        self.theSlider.sl.valueChanged.connect(self.image2.clear)
        self.theSlider.sl.valueChanged.connect(self.refresh)

            
        
        p = self.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        self.image2.move(p)
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    def getMapImage(lat, lng, zoom):
            urlbase = "http://maps.google.com/maps/api/staticmap?"
            GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
            args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
            args = args + "&key=" + GOOGLEAPIKEY
            mapURL = urlbase+args
            urlretrieve(mapURL, 'googlemap.png')
            
            '''
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('googlemap.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        
        self.show()
        
#slider code

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        theSlider = sliderdemo(self)
        #googleImage = App()
        
        self.setGeometry(800,800,1600,800)
        self.setWindowTitle("PyQt5 Slider")
        self.setWindowIcon(QIcon("python.png"))
        #self.hbox = QHBoxLayout()
        #self.gps = QWidget(self)
        self.left = 1000
        self.top = 1000
        self.width = 640
        self.height = 480
        # self.resize(self.width(), self.height())
        
        # self.GPS()
        #layout = QVBoxLayout()
        theSlider = sliderdemo(self)
        self.setCentralWidget(theSlider)
        
        layout.addWidget(theSlider)
        #layout.addWidget(googleImage)
        self.setLayout(layout)
        self.show()
'''
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
      self.setWindowTitle("GPS slider")

      self.label = QLabel("12", self)

   def valuechange(self):
      self.label.setText(str(self.sl.value()))
      App.getMapImage(43, -96, self.sl.value())


      
      '''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    # ex = sliderdemo()
    # ex.show()
    win.show()

    #sys.exit(app.exec_())
    app.exec()
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensize = app.desktop().availableGeometry().size()

    ex = ExampleWindow(screensize)
    ex.show()

sys.exit(app.exec_())
