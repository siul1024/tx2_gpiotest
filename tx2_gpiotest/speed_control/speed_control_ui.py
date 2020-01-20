# -*- coding: utf-8 -*-
# 한글표시
from PyQt5 import uic, QtWidgets
# from adafruit_servokit import ServoKit

class Speed_Control(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = uic.loadUi("speed_control.ui")
        self.ui.show()

        self.v_speed = 90    # 회전 방향 default
        self.l_speed = 0    # 직진 속도 default
        # self.kit = ServoKit(channels=8)

        self.ui.btn_a.setCheckable(True)


        self.ui.btn_w.clicked.connect(self.sp_u)    # alt + w 입력시 직진속도 +
        self.ui.btn_s.clicked.connect(self.sp_d)    # alt + s 입력시 직진속도 -
        self.ui.btn_a.pressed.connect(self.sp_l)    # alt + a 입력시 회전 방향 -
        self.ui.btn_d.clicked.connect(self.sp_r)    # alt + d 입력시 회전 방향 +
        self.ui.btn_stop.clicked.connect(self.sp_s) # alt + f 입력시 속도 0

    def sp_u(self):
        self.l_speed = self.l_speed + 10
        self.Status()

    def sp_d(self):
        self.l_speed = self.l_speed - 10
        self.Status()

    def sp_l(self):
        self.v_speed = self.v_speed - 10

        if self.v_speed <0:
            self.v_speed=0

        self.Status()

    def sp_r(self):
        self.v_speed = self.v_speed + 10

        if self.v_speed >180:
            self.v_speed=180

        self.Status()

    def sp_s(self):
        self.l_speed = 0
        self.v_speed = 90
        self.Status()

    def Status(self):   # 상태 표시
        if (self.l_speed > 0):  # 전진 속도 및 상태 표시
            self.ui.lbl_show_ls.setText(str(self.l_speed)+' 전진')
        elif(self.l_speed == 0):
            self.ui.lbl_show_ls.setText(str(self.l_speed) + ' 정지')
        else:
            self.ui.lbl_show_ls.setText(str(self.l_speed) + ' 후진')

        if (self.v_speed < 90):  # 회전 방향 및 수치 표시
            self.ui.lbl_show_vs.setText(str(self.v_speed)+' 좌회전')
        elif(self.v_speed == 90):
            self.ui.lbl_show_vs.setText(str(self.v_speed)+' 직진')
        else:
            self.ui.lbl_show_vs.setText(str(self.v_speed)+' 우회전')

        # self.kit.servo[2].angle = self.v_speed