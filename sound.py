#! /usr/bin/python

from os import system
from time import sleep

while True:
	activate = open('/tmp/activate', 'r')
	if activate.read(1) == '1':
		system('omxplayer -o local file.mp3 &')
		sleep(3.5)
	activate.close()
	sleep(0.01)
