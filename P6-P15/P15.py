#P15.py
#Sullivan Dahan - - Lefevre
pinStepX =  54
pinDirX = 55
pinEnableX = 38
pinStepY = 60
pinDirY = 61
pinEnableY = 56
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
#Declaration des pin Y
rpi.pinMode(pinStepY, rpi.OUTPUT)
rpi.pinMode(pinDirY, rpi.OUTPUT)
rpi.pinMode(pinEnableY, rpi.OUTPUT)

#Desactivation du frein X
rpi.digitalWrite(pinEnableX, rpi.LOW)
rpi.digitalWrite(pinDirX, rpi.LOW)

for i in range(3400):
        rpi.digitalWrite(pinStepX, rpi.HIGH)
        rpi.digitalWrite(pinStepX, rpi.LOW)

#Desactivation du frein Y
rpi.digitalWrite(pinEnableY, rpi.LOW)
rpi.digitalWrite(pinDirY, rpi.LOW)

for i in range(2250):
        rpi.digitalWrite(pinStepY, rpi.HIGH)
        rpi.digitalWrite(pinStepY, rpi.LOW)
print("P15")
