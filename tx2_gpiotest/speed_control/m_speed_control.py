from PyQt5 import QtWidgets

from MainWindow_ui import Main_Control

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Main_Control()
    app.exec_()

