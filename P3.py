#P3.py
#Elias
pinStepX =  54
pinDirX = 55
pinEnableX = 38
pinStepY = 60
pinDirY = 61
pinEnableY = 56
i=0

#Import des bibliothèques
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

#Ping l'arduino
connection = SerialManager(device='/dev/ttyACM0')
rpi=ArduinoApi(connection=connection)

#Déclaration des pin X
rpi = ArduinoApi()
rpi.pinMode(pinStepX, rpi.OUTPUT)
rpi.pinMode(pinDirX, rpi.OUTPUT)
rpi.pinMode(pinEnableX, rpi.OUTPUT)
#Déclaration des pin Y
rpi.pinMode(pinStepY, rpi.OUTPUT)
rpi.pinMode(pinDirY, rpi.OUTPUT)
rpi.pinMode(pinEnableY, rpi.OUTPUT)

#Désactivation du frein X
rpi.digitalWrite(pinEnableX, rpi.LOW)
rpi.digitalWrite(pinDirX, rpi.LOW)

for i in range(5000):
        rpi.digitalWrite(pinStepX, rpi.HIGH)
        rpi.digitalWrite(pinStepX, rpi.LOW)

#Désactivation du frein Y
rpi.digitalWrite(pinEnableY, rpi.LOW)
rpi.digitalWrite(pinDirY, rpi.LOW)

for i in range(?):
        rpi.digitalWrite(pinStepY, rpi.HIGH)
        rpi.digitalWrite(pinStepY, rpi.LOW)
print("P2")

except:
    print("fin")
