from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
# import Jetson.GPIO as GPIO

# pin
led_pin = 12   # BOARD pin 12


class GPIO_Ui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("widget.ui")
        self.ui.setWindowTitle("GPIO test")
        self.ui.show()
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(led_pin, GPIO.OUT)  # set as output
        # GPIO.output(led_pin, GPIO.LOW)
        self.ui.btn_up.clicked.connect(self.light_on)
        self.ui.btn_down.clicked.connect(self.light_off)

    def light_on(self):
        # GPIO.output(led_pin, GPIO.HIGH)
        self.ui.label_2.setText("HIGH")

    def light_off(self):
        # GPIO.output(led_pin, GPIO.LOW)
        self.ui.label_2.setText("LOW")


if __name__ == "__main__":
    app = QApplication([])
    w = GPIO_Ui()
    app.exec_()