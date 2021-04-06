#initialisation_X.py
#Sullivan Dahan - - Lefèvre
pinMaxX = 2
pinMinX = 3
pinStepX =  54
pinDirX = 55
pinEnableX = 38
i=1

#Import des bibliothèques
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

#Ping l'arduino
connection = SerialManager(device='/dev/ttyACM0')
rpi=ArduinoApi(connection=connection)

#Déclaration des pin
rpi = ArduinoApi()
rpi.pinMode(pinStepX, rpi.OUTPUT)
rpi.pinMode(pinDirX, rpi.OUTPUT)
rpi.pinMode(38, rpi.OUTPUT)
rpi.pinMode(pinMinX, rpi.INPUT)
rpi.pinMode(pinMaxX, rpi.INPUT)

#
rpi.digitalWrite(pinEnableX, rpi.LOW)
rpi.digitalWrite(pinDirX, rpi.HIGH)

pinMin = rpi.digitalRead(pinMinX)
while pinMin != i:
    rpi.digitalWrite(pinStepX, rpi.HIGH)
    sleep(0.00005)
    rpi.digitalWrite(pinStepX, rpi.LOW)
    sleep(0.00005)
    pinMin = rpi.digitalRead(pinMinX)
