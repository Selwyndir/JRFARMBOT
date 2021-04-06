#P5.py
#Djallil
pinMaxX = 2
pinMinX = 3
pinStepX =  54
pinDirX = 55
pinEnableX = 38
i=0

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
rpi.pinMode(pinEnableX, rpi.OUTPUT)
rpi.pinMode(pinMinX, rpi.INPUT)
rpi.pinMode(pinMaxX, rpi.INPUT)

#
rpi.digitalWrite(pinEnableX, rpi.LOW)
rpi.digitalWrite(pinDirX, rpi.HIGH)

pinMin = rpi.digitalRead(pinMinX)
while pinMin != 1:
    rpi.digitalWrite(pinStepX, rpi.HIGH)
    sleep(0.00005)
    rpi.digitalWrite(pinStepX, rpi.LOW)
    sleep(0.00005)
    pinMin = rpi.digitalRead(pinMinX)



#Désactivation du frein
rpi.digitalWrite(pinEnableX, rpi.LOW)
rpi.digitalWrite(pinDirX, rpi.LOW)


for i in range(34000):
        rpi.digitalWrite(pinStepX, rpi.HIGH)
        rpi.digitalWrite(pinStepX, rpi.LOW)
print("P5")

except:
    print("fin")
