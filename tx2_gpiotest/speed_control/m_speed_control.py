from PyQt5 import QtWidgets

from tx2_gpiotest.speed_control.speed_control_ui import Speed_Control

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Speed_Control()
    app.exec_()

