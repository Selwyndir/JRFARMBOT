#initialisation_Y.py
#Sullivan Dahan - - Lefevre
pinMaxY = 15
pinMinY = 14
pinStepY =  60
pinDirY = 61
pinEnableY = 56
i=0

#Import des bibliotheques
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

#Ping l'arduino
connection = SerialManager(device='/dev/ttyACM0')
rpi=ArduinoApi(connection=connection)

#Declaration des pin
rpi.pinMode(pinStepY, rpi.OUTPUT)
rpi.pinMode(pinDirY, rpi.OUTPUT)
rpi.pinMode(pinEnableY, rpi.OUTPUT)
rpi.pinMode(pinMinY, rpi.INPUT)
rpi.pinMode(pinMaxY, rpi.INPUT)

#
rpi.digitalWrite(pinEnableY, rpi.LOW)
rpi.digitalWrite(pinDirY, rpi.HIGH)

pinMin = rpi.digitalRead(pinMinY)
while pinMin != 0:
    rpi.digitalWrite(pinStepY, rpi.HIGH)
    sleep(0.00005)
    rpi.digitalWrite(pinStepY, rpi.LOW)
    sleep(0.00005)
    pinMin = rpi.digitalRead(pinMinY)
