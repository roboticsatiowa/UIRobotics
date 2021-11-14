from urllib.request import urlopen, urlretrieve
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
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.theSlider = sliderdemo(self)

        layout_box = QHBoxLayout(self.widget)
        layout_box.addWidget(self.theSlider)
        self.pixmap2 = QPixmap(App.getMapImage(44, -96, self.theSlider.sl.value()))
        self.image2 = QLabel(self.widget)
        self.image2.setPixmap(self.pixmap2)
        self.image2.setFixedSize(self.pixmap2.size())
        self.theSlider.sl.valueChanged.connect(self.refresh)

        p = self.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        self.image2.move(p)


    def refresh(self):

        self.image2.clear()
        self.pixmap2 = QPixmap('googlemap.png')
        self.image2.setPixmap(self.pixmap2)
        self.image2.setFixedSize(self.pixmap2.size())


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'GPS'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 450
        self.initUI()
    def getMapImage(lat, lng, zoom):
            urlbase = "http://maps.google.com/maps/api/staticmap?"
            GOOGLEAPIKEY = "AIzaSyCHD0L-s_gWE6VTNumgn1TMCEhiDTEok_U"
            args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers=color:red|size:small|{},{}|".format(lat,lng,zoom,400,400,"hybrid",lat,lng)
            args = args + "&key=" + GOOGLEAPIKEY
            mapURL = urlbase+args
            urlretrieve(mapURL, 'googlemap.png')
            img = QPixmap('googlemap.png')
            return img


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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensize = app.desktop().availableGeometry().size()

    ex = ExampleWindow(screensize)
    ex.show()

sys.exit(app.exec_())
