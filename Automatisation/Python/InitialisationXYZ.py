#InitialisationXYZ.py
#Association des Pins à des Variables
#X
pinMaxX = 2
pinMinX = 3
pinStepX =  54
pinDirX = 55
pinEnableX = 38
#Y
pinMaxY = 15
pinMinY = 14
pinStepY =  60
pinDirY = 61
pinEnableY = 56
#Z
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

#Declaration des pin X
rpi.pinMode(pinStepX, rpi.OUTPUT)
rpi.pinMode(pinDirX, rpi.OUTPUT)
rpi.pinMode(pinEnableX, rpi.OUTPUT)
rpi.pinMode(pinMinX, rpi.INPUT)
rpi.pinMode(pinMaxX, rpi.INPUT)
#Declaration des pin Y
rpi.pinMode(pinStepY, rpi.OUTPUT)
rpi.pinMode(pinDirY, rpi.OUTPUT)
rpi.pinMode(pinEnableY, rpi.OUTPUT)
rpi.pinMode(pinMinY, rpi.INPUT)
rpi.pinMode(pinMaxY, rpi.INPUT)
#Declaration des pin Z
rpi.pinMode(pinStepZ, rpi.OUTPUT)
rpi.pinMode(pinDirZ, rpi.OUTPUT)
rpi.pinMode(pinEnableZ, rpi.OUTPUT)
rpi.pinMode(pinMinZ, rpi.INPUT)
rpi.pinMode(pinMaxZ, rpi.INPUT)

#Desactivation du frein et choix de la Direction de X
rpi.digitalWrite(pinEnableX, rpi.LOW)
rpi.digitalWrite(pinDirX, rpi.HIGH)
#Desactivation du frein et choix de la Direction de Y
rpi.digitalWrite(pinEnableY, rpi.LOW)
rpi.digitalWrite(pinDirY, rpi.HIGH)
#Desactivation du frein et choix de la Direction de Z
rpi.digitalWrite(pinEnableZ, rpi.LOW)
rpi.digitalWrite(pinDirZ, rpi.HIGH)

#InitialisationX
XpinMin = rpi.digitalRead(pinMinX)
while XpinMin != 0:
    rpi.digitalWrite(pinStepX, rpi.HIGH)
    sleep(0.00005)
    rpi.digitalWrite(pinStepX, rpi.LOW)
    sleep(0.00005)
    XpinMin = rpi.digitalRead(pinMinX)
#InitialisationY
YpinMin = rpi.digitalRead(pinMinY)
while YpinMin != 0:
    rpi.digitalWrite(pinStepY, rpi.HIGH)
    sleep(0.00005)
    rpi.digitalWrite(pinStepY, rpi.LOW)
    sleep(0.00005)
    YpinMin = rpi.digitalRead(pinMinY)
#InitialisationZ
ZpinMin = rpi.digitalRead(pinMinZ)
while ZpinMin != 0:
    rpi.digitalWrite(pinStepZ, rpi.HIGH)
    sleep(0.00005)
    rpi.digitalWrite(pinStepZ, rpi.LOW)
    sleep(0.00005)
    ZpinMin = rpi.digitalRead(pinMinZ)
