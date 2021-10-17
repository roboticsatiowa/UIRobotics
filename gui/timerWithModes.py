# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
    	super().__init__()

    	# setting title
    	self.setWindowTitle("Timer")

    	# setting geometry
    	self.setGeometry(800,800,1000,800)

    	# calling method
    	self.UiComponents()

    	# showing all the widgets
    	self.show()

    # method for widgets
    def UiComponents(self):

    	# variables
    	# count variable
        self.count = 0

    	# start flag
        self.start = False

    	# creating push button to get time in seconds
        button = QPushButton("Set time", self)
        button.setGeometry(500, 100, 150, 50)
        button.clicked.connect(self.get_seconds)

    	# creating label to show the seconds
        self.label = QLabel("//TIMER//", self)
        self.label.setGeometry(425, 200, 300, 50)
        self.label.setStyleSheet("border : 3px solid black")
        self.label.setFont(QFont('Times', 15))
        self.label.setAlignment(Qt.AlignCenter)

    	# creating start button
        start_button = QPushButton("Start", self)
        start_button.setGeometry(500, 300, 150, 50)
        start_button.clicked.connect(self.start_action)

        # creating pause button
        pause_button = QPushButton("Pause", self)
        pause_button.setGeometry(500, 370, 150, 50)
        pause_button.clicked.connect(self.pause_action)

    	# creating reset button
        reset_button = QPushButton("Reset", self)
        reset_button.setGeometry(500, 440, 150, 50)
        reset_button.clicked.connect(self.reset_action)

    	# creating a timer object
        timer = QTimer(self)
		# adding action to timer
        timer.timeout.connect(self.showTime)
		# update the timer every tenth second
        timer.start(100)

        # creating stop button
        stopButton = QPushButton("STOP ROVER", self)
        stopButton.setGeometry(125, 320, 200, 50)
        stopButton.clicked.connect(self.stop_action)

        # creating auto mode button
        autoButton = QPushButton("AUTO MODE", self)
        autoButton.setGeometry(125, 440, 200, 50)
        autoButton.clicked.connect(self.auto_action)

        # creating manual mode button
        manualButton = QPushButton("MANUAL MODE", self)
        manualButton.setGeometry(125, 380, 200, 50)
        manualButton.clicked.connect(self.manual_action)


    # method called by stop button
    def stop_action(self):
        print("ROVER STOPPED")

    # method called by auto mode button
    def auto_action(self):
        print("ROVER IN AUTO MODE")

    # method called by manual mode button
    def manual_action(self):
        print("ROVER IN MANUAL MODE")

	# method called by timer
    def showTime(self):

		# checking if flag is true
        if self.start:
			# incrementing the counter
            self.count -= 1

			# timer is completed
            if self.count == 0:

				# making flag false
                self.start = False

				# setting text to the label
                self.label.setText("Completed !!!! ")

        if self.start:
			# getting text from count
            text = str(self.count / 10) + " s"

			# showing text
            self.label.setText(text)


	# method called by the push button
    def get_seconds(self):

		# making flag false
        self.start = False

		# getting seconds and flag
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

		# if flag is true
        if done:
			# changing the value of count
            self.count = second * 10

			# setting text to the label
            self.label.setText(str(second))

    def start_action(self):
		# making flag true
        self.start = True

		# count = 0
        if self.count == 0:
            self.start = False

    def pause_action(self):

		# making flag false
        self.start = False

    def reset_action(self):

		# making flag false
        self.start = False

		# setting count value to 0
        self.count = 0

		# setting label text
        self.label.setText("//TIMER//")



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
