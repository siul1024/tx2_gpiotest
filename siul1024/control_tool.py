from PyQt5 import uic, QtWidgets
import curses
import time
import Adafruit_PCA9685


class CarControlUi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = uic.loadUi("control_tool.ui")
        self.ui.setWindowTitle("remote control")
        self.ui.show()
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

