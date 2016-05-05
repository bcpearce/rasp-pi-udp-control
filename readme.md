# UDP Controlled Robot

This project contains python scripts for Raspberry Pi to control a robot using UDP commands.  

## Hardware 

To control the motors, a SainSmart L298N motor controller with two outputs was used.
The pins must be assigned in the `pins.json` file according to the pin labels on the L298N.

## Running

Run with `python udp_motor_control.py [ip_address]` on the Raspberry Pi.

## Command Format

The scripts process UDP sent as strings.  The string must be of format `"{right motor power} {left motor power} {right motor direction} {left motor direction}"`.  The parameters must be separated by spaces.  The power parameters must be between 0 and 100, and may be floats.

## P-D Control

In order to smooth out the turning, speeding up, and slowing down, a P-D controller is implemented on speed changes.  The parameters are currently fixed at `kP = 1` and `kD = 0.25`.
