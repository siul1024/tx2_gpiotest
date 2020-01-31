

# define
import curses
import sys


class TestCarControl:
    channel_t = 0
    channel_s = 7
    throttle_stop = 290
    steering_center = 350
    throttle_bwd = 350
    throttle_fwd = 220
    steering_r = 420  # 420
    steering_l = 280  # 280
    pulse_freq = 50

    def __init__(self):
        self.throttle = TestCarControl.throttle_stop
        self.steering = TestCarControl.steering_center
        self.mode = True

    def moving_stop(self):
        self.mode = False

    def turn_left(self):
        if self.steering > TestCarControl.steering_l:
            self.steering -= 14
        self.__write_val()

    def turn_right(self):
        if self.steering < TestCarControl.steering_r:
            self.steering += 14
        self.__write_val()

    def run_forward(self):
        if self.throttle > TestCarControl.throttle_fwd:
            if self.throttle == TestCarControl.throttle_stop:
                self.throttle = TestCarControl.throttle_stop - 18
            self.throttle -= 1
        self.__write_val()

    def run_backward(self):
        if self.throttle < TestCarControl.throttle_bwd:
            if self.throttle == TestCarControl.throttle_stop:
                self.throttle = TestCarControl.throttle_stop + 18
            self.throttle += 1
        self.__write_val()

    def car_brake(self):
        self.throttle = TestCarControl.throttle_stop
        self.__write_val()

    def __write_val(self):
        self.__throttle_assist()

    def steering_assist(self):
        if self.steering > TestCarControl.steering_center:
            self.steering -= 14
        elif self.steering < TestCarControl.steering_center:
            self.steering += 14
        if (self.steering < TestCarControl.steering_center + 10) \
                & (self.steering > TestCarControl.steering_center - 10):
            self.steering = TestCarControl.steering_center
        self.__write_val()

    def __throttle_assist(self):
        if (self.throttle <= TestCarControl.throttle_stop + 18) \
                & (self.throttle >= TestCarControl.throttle_stop - 18):
            self.throttle = TestCarControl.throttle_stop

