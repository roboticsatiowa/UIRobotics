import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QStatusBar, QToolBar
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

from functools import partial

import sys


# def window():
#     app = QApplication(sys.argv)
#     widget = QWidget()
#
#     widget.setGeometry(0,0,1200,800)
#     widget.setWindowTitle("Runtime GUI")
#
#     textLabel = QLabel(widget)
#     textLabel.setText("Hello World!")
#     textLabel.move(110,85)
#
#     button1 = QPushButton(widget)
#     button1.setText("Button1")
#     button1.move(64,32)
#
#
#     widget.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#    window()



        # self._createMenu()
        # self._createToolBar()
        # self._createStatusBar()
    #
    # def _createMenu(self):
    #     self.menu = self.menuBar().addMenu("&Menu")
    #     self.menu.addAction('&Exit', self.close)
    #
    # def _createToolBar(self):
    #     tools = QToolBar()
    #     self.addToolBar(tools)
    #     tools.addAction('Exit', self.close)
    #
    # def _createStatusBar(self):
    #     status = QStatusBar()
    #     status.showMessage("I'm the Status Bar")
    #     self.setStatusBar(status)


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Robotics at Iowa ')
        self.setFixedSize(1000, 500)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createButtons()

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {'STOP': (0, 0),
                   'AUTO': (0, 1),
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(100, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)


    def printTestStop(self):
        print("STOP")

    def printTestAuto(self):
        print("AUTO")

class Ctrl:
    """Controller class."""
    def __init__(self, win):
        """Controller initializer."""
        self._win = win
        self._connectSignals()

    def _connectSignals(self):
        """Connect signals and slots."""
        self._win.buttons['AUTO'].clicked.connect(self._win.printTestAuto)
        self._win.buttons['STOP'].clicked.connect(self._win.printTestStop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    Ctrl(win=win)
    sys.exit(app.exec_())
