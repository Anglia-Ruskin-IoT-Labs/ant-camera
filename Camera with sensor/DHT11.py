#!/usr/bin/python
#import libraries
import sys
import Adafruit_DHT
import time

#using the DHT11 sensor
sensor=Adafruit_DHT.DHT11
#setting pin 4 to General purpose input output
gpio=4

#continous loop
while True:

#get the readings of the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
#convert the variables to string
    repr(humidity)
    repr(temperature)

#open a text file to write
    with open('reading.txt','w') as f:
#write to the file
        f.write(repr(temperature) + "* " + repr(humidity) + "%")
#delay for 0.2 seconds
    time.sleep(0.2)
