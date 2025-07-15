#!/usr/bin/python

import socket
import RPi.GPIO as GPIO
import time

servoPIN = 17  #  Door Servo
servoPIN2 = 27   #  Capture Servo

time.sleep(15)

def openservo():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(servoPIN, GPIO.OUT)
 p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
 p.start(2.5) # Initialization
 p.ChangeDutyCycle(2)
 time.sleep(0.5)
 p.ChangeDutyCycle(12)
 time.sleep(0.5)
 p.stop()
 GPIO.cleanup()

#def closeservo():
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servoPIN, GPIO.OUT)
# p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
# p.start(2.5) # Initialization
# p.ChangeDutyCycle(12)
# time.sleep(0.5)
# p.ChangeDutyCycle(2)
# time.sleep(0.5)
# p.stop()
# GPIO.cleanup()

def closeservo():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(servoPIN, GPIO.OUT)
 p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
 p.start(0) # Initialization
 p.ChangeDutyCycle(2.0)  # -90 degrees
# time.sleep(0.5)
 p.ChangeDutyCycle(2.5) # Turn to neutral pos (0 deg pos)
 time.sleep(0.5)
# p.ChangeDutyCycle(0) # +90 degree
# time.sleep(0.5)
# p.stop(0) # ending on 0 position
 p.stop() # ending on 0 position
 GPIO.cleanup()

def captureservo():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(servoPIN2, GPIO.OUT)
 p = GPIO.PWM(servoPIN2, 50) # GPIO 27 for PWM with 50Hz
 p.start(2.5) # Initialization
 p.ChangeDutyCycle(2)
 time.sleep(0.5)
 p.ChangeDutyCycle(12)
 time.sleep(0.5)
 p.ChangeDutyCycle(2)
 time.sleep(0.5)
 p.ChangeDutyCycle(12)
 time.sleep(0.5)
 p.stop()
 GPIO.cleanup()

closeservo()


