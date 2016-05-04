#!/usr/bin/python

import RPi.GPIO as GPIO

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
        self.pwm.ChangeDutyCycle(duty_pct)

    def set_fwd(self):
        GPIO.output(ctrl_pin1, 1)
        GPIO.output(ctrl_pin2, 0)

    def set_rev(self):
        GPIO.output(ctrl_pin1, 0)
        GPIO.output(ctrl_pin2, 1)


