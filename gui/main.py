import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QStatusBar, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

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

import sys

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
