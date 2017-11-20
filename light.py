#! /usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(6, GPIO.OUT)
while True:
	activate = open('/tmp/activate')
	if open.read(1) == '1':
		GPIO.output(6, True)
	else:
		GPIO.output(6, False)
	activate.close()
	sleep(0.01)
