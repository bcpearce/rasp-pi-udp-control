#!/usr/bin/python
import sys, asyncore
from motor_driver import MotorDriver
from async_udp_receiver import AsyncUdpReceiver

if __name__ == "__main__":
    PIN_DICT = {'ENA':21, 'ENB':16, 
                'IN1':13, 'IN2':20, 
                'IN3':26, 'IN4':19}

    s1_pins = [PIN_DICT[key] for key in ['ENA', 'IN1', 'IN2']]
    servo1 = MotorDriver(*s1_pins)

    s2_pins = [PIN_DICT[key] for key in ['ENB', 'IN3', 'IN4']]
    servo2 = MotorDriver(*s2_pins)

    try:
        ip = sys.argv[1]
        port = 5000
        server = AsyncUdpReceiver(ip, port, servo1, servo2)
        print 
        print "Opening socket on {0}:{1}".format(ip, port)
        print "Waiting for data..."
        asyncore.loop()

    finally:
        servo1.stop()
        servo2.stop()
