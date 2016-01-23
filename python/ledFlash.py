#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led=17

GPIO.setup(led,GPIO.OUT)

print("Light On")
GPIO.output(led,GPIO.HIGH)

time.sleep(1)
print("Light Off")
GPIO.output(led,GPIO.LOW)

time.sleep(1)
print("Light On")
GPIO.output(led,GPIO.HIGH)

time.sleep(1)
print("Light Off")
GPIO.output(led,GPIO.LOW)
time.sleep(1)
print("Light On")
GPIO.output(led,GPIO.HIGH)

time.sleep(1)
print("Light Off")
GPIO.output(led,GPIO.LOW)
time.sleep(1)
print("Light On")
GPIO.output(led,GPIO.HIGH)

time.sleep(1)
print("Light Off")
GPIO.output(led,GPIO.LOW)
time.sleep(1)
print("Light On")
GPIO.output(led,GPIO.HIGH)

time.sleep(1)
print("Light Off")
GPIO.output(led,GPIO.LOW)

GPIO.cleanup()
