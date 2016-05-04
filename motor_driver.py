#!/usr/bin/python

class MotorDriver:

    def __init__(self, spd_pin, ctrl_pin1, ctrl_pin2, **kwargs):

        if GPIO.setmode() < 0:
            GPIO.setmode(GPIO.BCM)

        self.spd_pin = spd_pin
        self.ctrl_pins = (ctrl_pin1, ctrl_pin2)
        self.spd = 0

        # change pins output 0
        for pin in self.ctrl_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        # set spd pin to PWM, default to 50Hz
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(PIN_DICT['ENA'], kwargs.get('hz', 50))

    def start(self, duty_pct):
        self.pwm.start(duty_pct)

    def stop(self):
        self.pwm.stop()

    def set_spd(self, duty_pct):
        self.pwm.ChangeDutyCycle(duty_pct)

    def __del__(self):
        self.pwm.stop()


