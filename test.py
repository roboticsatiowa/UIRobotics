from PyQt5.Qt import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtCore import Qt
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json
import webbrowser

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

        zm = 3

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

        # pixmap = pixmap.scaled(700, 800, Qt.KeepAspectRatio, Qt.FastTransformation)
    # lat = input("Enter latitude: ")
    # while not ifValidLatitude(lat):
    #     lat = input("Enter latitude: ")
    #
    # lng = input("Enter longitude: ")
    # while not ifValidLongitude(lng):
    #     lng = input("Enter longitude: ")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GPS()
    sys.exit(app.exec_())
