#LumiereAuto.py 
Lampe = 9
LUM_PIN = 57

from nanpy import (ArduinoApi, SerialManager)
from time import sleep

connection = SerialManager(device='/dev/ttyACM0')
rpi=ArduinoApi(connection=connection)

rpi.pinMode(Lampe, rpi.OUTPUT)
rpi.pinMode(LUM_PIN, rpi.INPUT)

Lumino = rpi.digitalRead(LUM_PIN)
while True :
    if Lumino = 1 : 
    rpi.digitalWrite(Lampe, rpi.LOW)
    elif Lumino = 0:
    rpi.digitalWrite(Lampe, rpi.HIGH)
