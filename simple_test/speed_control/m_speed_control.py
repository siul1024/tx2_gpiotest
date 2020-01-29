from PyQt5 import QtWidgets

from simple_test.speed_control.speed_control_ui import Speed_Control

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Speed_Control()
    app.exec_()

