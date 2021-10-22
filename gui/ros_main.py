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
import rospy
from std_msgs.msg import String


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Robotics at Iowa GUI')
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
        buttons = {'AUTO': (0, 0),
                   'TELEOP': (0,1)
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(150, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)


    def sendAuto(self):
        msg="AUTO"
        pub_mode.publish(msg)

    def sendTeleop(self):
        msg="TELEOP"
        pub_mode.publish(msg)

class Ctrl:
    """Controller class."""
    def __init__(self, win):
        """Controller initializer."""
        self._win = win
        self._connectSignals()

    def _connectSignals(self):
        """Connect signals and slots."""
        self._win.buttons['AUTO'].clicked.connect(self._win.sendAuto)
        self._win.buttons['TELEOP'].clicked.connect(self._win.sendTeleop)


if __name__ == '__main__':
    rospy.init_node('ROSgui', anonymous=True)
    pub_mode=rospy.Publisher('mode', String, queue_size=10)

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    Ctrl(win=win)
    sys.exit(app.exec_())