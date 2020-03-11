from PyQt5 import uic, QtWidgets, QtCore
import cv2, sys, time
import threading

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap

from remote_control_key.car_control import CarControl
# from siul1024.test.uitest import TestCarControl

onboard_cam = "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=640, height=480,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
real_cam = 1

width = 640
height = 480


class ControlToolUi(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # video open
        self.cap1 = cv2.VideoCapture(real_cam)  # real_cam
        self.cap2 = cv2.VideoCapture(onboard_cam)  # onboard_cam
        self.running = True
        # car control class
        self.myCar = CarControl()
        # self.myCar = TestCarControl()
        # init ui
        self.ui = self.__init_ui()
        self.ui.installEventFilter(self)
        # threading
        self.th1 = threading.Thread(target=self.open_camera)
        self.th1.start()
        self.th2 = threading.Thread(target=self.move)
        self.th2.start()

    def __init_ui(self):
        ui = uic.loadUi("remote_control_key/control_tool.ui")
        ui.setWindowTitle("remote control")
        # button signal & slot
        ui.btn_right.pressed.connect(self.myCar.turn_right)
        ui.btn_left.pressed.connect(self.myCar.turn_left)
        ui.btn_up.pressed.connect(self.myCar.run_forward)
        ui.btn_down.pressed.connect(self.myCar.run_backward)
        ui.btn_stop.pressed.connect(self.myCar.car_brake)
        # widget close event
        ui.closeEvent = self.closeEvent
        return ui

    # Qt Event Filter
    def eventFilter(self, obj, event):
        try:
            if event.type() == QtCore.QEvent.KeyPress:
                if event.key() == Qt.Key_Escape:
                    self.closeEvent()
                elif event.key() == Qt.Key_Up:
                    self.myCar.run_forward()
                elif event.key() == Qt.Key_Down:
                    self.myCar.run_backward()
                elif event.key() == Qt.Key_Left:
                    self.myCar.turn_left()
                elif event.key() == Qt.Key_Right:
                    self.myCar.turn_right()
                elif event.key() == Qt.Key_Space:
                    self.myCar.car_brake()
        finally:
            # self.ui.label_text.setText('steering: {},  throttle: {}'.format(self.myCar.steering, self.myCar.throttle))
            return super().eventFilter(obj, event)

    # move threading
    def move(self):
        while self.running:
            self.myCar.steering_assist()
            time.sleep(0.2)
            self.ui.label_text.setText('steering: {},  throttle: {}'.format(self.myCar.steering, self.myCar.throttle))

    # camera threading
    def open_camera(self):
        while self.running:
            ControlToolUi.__open_camera(self.cap1, self.ui.label_fwd)
            ControlToolUi.__open_camera(self.cap2, self.ui.label_bwd)

    @staticmethod
    def __open_camera(cap, label):
        try:
            ret, frame = cap.read()
            if ret:
                swap_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = swap_frame.shape
                qimg = QImage(swap_frame, w, h, ch * w, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg)
                label.setPixmap(pixmap)
        except KeyboardInterrupt:
            pass

    def th_stop(self):
        self.running = False
        time.sleep(0.3)

    def closeEvent(self, event):
        self.th_stop()
        self.cap1.release()
        self.cap2.release()
        self.deleteLater()
        event.accept()
        print('Window closed')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = ControlToolUi()
    w.ui.show()
    sys.exit(app.exec_())
