from urllib.request import urlopen, urlretrieve
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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
lat = input("Enter latitude: ")
while not ifValidLatitude(lat):
    lat = input("Enter latitude: ")
lng = input("Enter longitude: ")
while not ifValidLongitude(lng):
    lng = input("Enter longitude: ")
    
class ExampleWindow(QMainWindow):
    def __init__(self, windowsize):
        super().__init__()
        self.windowsize = windowsize
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.windowsize)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.theSlider = slider(self)

        layout_box = QHBoxLayout(self.widget)
        layout_box.addWidget(self.theSlider)
        self.pixmap2 = QPixmap(GPS.getMapImage(lat, lng, self.theSlider.sl.value()))
        self.image2 = QLabel(self.widget)
        self.image2.setPixmap(self.pixmap2)
        self.image2.setFixedSize(self.pixmap2.size())
        self.theSlider.sl.valueChanged.connect(self.refresh)

        gpsGeomoetry = self.geometry().bottomRight() - self.image2.geometry().bottomRight() - QPoint(100, 100)
        self.image2.move(gpsGeomoetry)

    def refresh(self):
        self.image2.clear()
        self.pixmap2 = QPixmap('googlemap.png')
        self.image2.setPixmap(self.pixmap2)
        self.image2.setFixedSize(self.pixmap2.size())

class GPS(QWidget):
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

class slider(QWidget):
   def __init__(self, parent):
      super(slider, self).__init__(parent)

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
      GPS.getMapImage(lat, lng, self.sl.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensize = app.desktop().availableGeometry().size()

    ex = ExampleWindow(screensize)
    ex.show()

sys.exit(app.exec_())
