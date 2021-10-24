# import sys
# from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QLabel, QMainWindow, QApplication, QGridLayout)
# from PyQt5.QtCore import Qt
#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(800,800,1600,800)
#         self.setWindowTitle("PyQt5 Slider")
#         # self.setWindowIcon(QIcon("python.png"))
#         self.hbox = QHBoxLayout()
#
#         self.slider = QSlider(self)
#     def theSlider():
#         slider = QSlider()
#
#         slider.setOrientation(Qt.Vertical)
#         slider.setTickPosition(QSlider.TicksBelow)
#         slider.setTickInterval(1)
#         slider.setMinimum(0)
#         slider.setValue(12)
#         slider.setMaximum(24)
#         slider.valueChanged.connect(changed_slider)
#         # hbox.addWidget(self.slider)
#     def changed_slider(self):
#         value = self.slider.value()
#         self.label.setText(str(value))
#         # zm = self.slider.value()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = Window()
#     win.show()
#     # Ctrl(win=win)
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QLabel, QMainWindow, QApplication, QGridLayout, QVBoxLayout)
from PyQt5.QtCore import Qt

class sliderdemo(QWidget):
   def __init__(self, parent = None):
      super(sliderdemo, self).__init__(parent)

      layout = QVBoxLayout()
      self.l1 = QLabel("Zoom")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)

      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(0)
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
      size = self.sl.value()
      self.label.setText(str(self.sl.value()))


def main():
   app = QApplication(sys.argv)
   ex = sliderdemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
