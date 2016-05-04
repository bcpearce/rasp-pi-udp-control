#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class MotorDriver:

    def __init__(self, spd_pin, ctrl_pin1, ctrl_pin2, **kwargs):

        GPIO.setmode(GPIO.BCM)

        self.spd_pin = spd_pin
        self.ctrl_pins = (ctrl_pin1, ctrl_pin2)
        self.spd = 0

        # change pins output 0
        for pin in self.ctrl_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        # set spd pin to PWM, default to 50Hz
        GPIO.setup(self.spd_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.spd_pin, kwargs.get('hz', 50))

    def start(self, duty_pct):
        self.pwm.start(duty_pct)

    def stop(self):
        self.pwm.stop()

    def set_spd(self, duty_pct):
        self.spd = duty_pct
        self.pwm.ChangeDutyCycle(duty_pct)

    def set_fwd(self):
        GPIO.output(self.ctrl_pins[0], 1)
        GPIO.output(self.ctrl_pins[1], 0)

    def set_rev(self):
        GPIO.output(self.ctrl_pins[0], 0)
        GPIO.output(self.ctrl_pins[1], 1)

    def set_off(self):
        GPIO.output(self.ctrl_pins[0], 0)
        GPIO.output(self.ctrl_pins[1], 0)

    def set_direction(self, direction):
        if direction.lower() == 'rev':
            self.set_rev()
        elif direction.lower() == 'fwd':
            self.set_fwd()
        else:
            self.set_off()

if __name__ == "__main__":

    PIN_DICT = {'ENA':21, 'ENB':16, 
                'IN1':13, 'IN2':20, 
                'IN3':26, 'IN4':19}

    s1_pins = [PIN_DICT[key] for key in ['ENA', 'IN1', 'IN2']]
    servo1 = MotorDriver(*s1_pins)

    s2_pins = [PIN_DICT[key] for key in ['ENB', 'IN3', 'IN4']]
    servo2 = MotorDriver(*s2_pins)

    servo1.set_fwd()
    servo2.set_rev()

    servo1.start(50)
    servo2.start(50)

    time.sleep(2)

    servo2.set_spd(100)
    servo1.set_off(100)

    time.sleep(2)


