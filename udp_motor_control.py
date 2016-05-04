#!/usr/bin/python
import RPi.GPIO as GPIO

if __name__ == "__main__":

    try:
        PIN_DICT = {'ENA':21, 'ENB':16, 
                    'IN1':13, 'IN2':20, 
                    'IN3':26, 'IN4':19}

        GPIO.setmode(GPIO.BCM)

        # all pins are output
        for val in PIN_DICT.values():
            GPIO.setup(val, GPIO.OUT)

        # set up pins to operate motors
        GPIO.output(PIN_DICT['IN1'], 1)
        GPIO.output(PIN_DICT['IN2'], 0)
        GPIO.output(PIN_DICT['IN3'], 1)
        GPIO.output(PIN_DICT['IN4'], 0)

        # run at 50Hz
        servo1 = GPIO.PWM(PIN_DICT['ENA'], 50)
        servo2 = GPIO.PWM(PIN_DICT['ENB'], 50)

        servo1.start(50.0)
        servo2.start(50.0)

        while True:
            pass

    finally:
        servo1.stop()
        servo2.stop()