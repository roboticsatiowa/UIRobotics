from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from UITest2 import Ui_GroupBox
from generateMap import getMapImage

class MainWindow(QGroupBox, Ui_GroupBox):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.count = 0
        self.start = False
        self.startTimer.clicked.connect(self.start_action)
        self.resetTimer.clicked.connect(self.reset_action)
        self.autonomous.clicked.connect(self.goAutonomous)
        self.manual.clicked.connect(self.goManual)
        self.thingButton.clicked.connect(lambda:getMapImage(38.266,-110.719))
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        
        
        self.show()

    def goAutonomous(self):
        print("yes")
        #have a way to make the rover switch to autonomous

    def goManual(self):
        print("yes")
        #have a way to make the rover switch to manual

        
         # method called by timer 
    def showTime(self):
        maps = QPixmap("googlemap.png")
        self.map.setPixmap(maps)
        
        # checking if flag is true 
        if self.start: 
            # incrementing the counter 
            self.count -= 1
  
            # timer is completed 
            if self.count == 0: 
  
                # making flag false 
                self.start = False
  
        if self.start:
            # getting text from count 
            text = int(self.count / 10) 
  
            # showing text 
            self.lcdNumber.display(text)
  
  
    # method called by the push button 
    def get_seconds(self):
        
        # if flag is true 
        if self.lineEdit.text()!= "" :

            second = int(self.lineEdit.text())
            
            # changing the value of count
            self.count = second * 10
            # setting text to the label 
            self.lcdNumber.display(second)

    def start_action(self):

        self.get_seconds()
        
        # making flag true 
        self.start = True

        # count = 0 
        if self.count == 0: 
            self.start = False
  
    #def pause_action(self): 
  
        # making flag false 
       # self.start = False
  
    def reset_action(self): 
  
        # making flag false 
        self.start = False
  
        # setting count value to 0 
        self.count = 0
  
        # setting label text 
        self.lcdNumber.display(0)
        self.lineEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
