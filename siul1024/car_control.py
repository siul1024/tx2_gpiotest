import curses, sys
import Adafruit_PCA9685


class CarControl:
    # define
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
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
        self.pwm.set_pwm_freq(CarControl.pulse_freq)
        self.throttle = CarControl.throttle_stop
        self.steering = CarControl.steering_center
        self.mode = True

    def moving_stop(self):
        self.mode = False

    def turn_left(self):
        if self.steering > CarControl.steering_l:
            self.steering -= 14
        self.__write_val()

    def turn_right(self):
        if self.steering < CarControl.steering_r:
            self.steering += 14
        self.__write_val()

    def run_forward(self):
        if self.throttle > CarControl.throttle_fwd:
            if self.throttle == CarControl.throttle_stop:
                self.throttle = CarControl.throttle_stop - 18
            self.throttle -= 1
        self.__write_val()

    def run_backward(self):
        if self.throttle < CarControl.throttle_bwd:
            if self.throttle == CarControl.throttle_stop:
                self.throttle = CarControl.throttle_stop + 18
            self.throttle += 1
        self.__write_val()

    def car_brake(self):
        self.throttle = CarControl.throttle_stop
        self.__write_val()

    def __write_val(self):
        self.__throttle_assist()
        self.pwm.set_pwm(CarControl.channel_t, 0, self.throttle)
        self.pwm.set_pwm(CarControl.channel_s, 0, self.steering)

    def steering_assist(self):
        if self.steering > CarControl.steering_center:
            self.steering -= 14
        elif self.steering < CarControl.steering_center:
            self.steering += 14
        if (self.steering < CarControl.steering_center + 10) & (self.steering > CarControl.steering_center - 10):
            self.steering = CarControl.steering_center
        self.__write_val()

    def __throttle_assist(self):
        if (self.throttle <= CarControl.throttle_stop + 18) & (self.throttle >= CarControl.throttle_stop - 18):
            self.throttle = CarControl.throttle_stop


def moving():
    car = CarControl()
    # curses.init
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.halfdelay(1)
    screen.keypad(True)
    try:
        while car.mode:
            char = screen.getch()
            screen.clear()
            if char == curses.KEY_DOWN:
                car.run_backward()
            elif char == curses.KEY_UP:
                car.run_forward()
            elif char == curses.KEY_RIGHT:
                car.turn_right()
            elif char == curses.KEY_LEFT:
                car.turn_left()
            elif char == ord('q') or char == ord('Q'):
                break
            elif char == ord('s') or char == ord('S'):
                car.car_brake()
            else:
                car.steering_assist()
            screen.addstr(0, 0, 'steering: ' + str(car.steering) + '\tthrottle :' + str(car.throttle))
    except KeyboardInterrupt:
        car.mode = False
    finally:
        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit()


if __name__ == '__main__':
    moving()
