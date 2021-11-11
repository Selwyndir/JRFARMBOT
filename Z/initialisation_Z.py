#initialisation_Z.py
pinMaxZ = 19
pinMinZ = 18
pinStepZ =  46
pinDirZ = 48
pinEnableZ = 62
i=0
#Import des bibliotheques
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
#Ping l'arduino
connection = SerialManager(device='/dev/ttyACM0')
rpi=ArduinoApi(connection=connection)
#Declaration des pin
rpi.pinMode(pinStepZ, rpi.OUTPUT)
rpi.pinMode(pinDirZ, rpi.OUTPUT)
rpi.pinMode(pinEnableZ, rpi.OUTPUT)
rpi.pinMode(pinMinZ, rpi.INPUT)
rpi.pinMode(pinMaxZ, rpi.INPUT)
#
rpi.digitalWrite(pinEnableZ, rpi.LOW)
rpi.digitalWrite(pinDirZ, rpi.HIGH)

pinMin = rpi.digitalRead(pinMinZ)
while pinMin != 0:
    rpi.digitalWrite(pinStepZ, rpi.HIGH)
    sleep(0.00005)
    rpi.digitalWrite(pinStepZ, rpi.LOW)
    sleep(0.00005)
    pinMin = rpi.digitalRead(pinMinZ)
