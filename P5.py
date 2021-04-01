#P1.py
# 2 = pinMax / 3 = pinMin
# 54 = pinStep 
# 55 = pinDir
# 38 = pinEnable
from nanpy import ArduinoApi
from time import *
i=0

try:
    connection = SerialManager()
    rpi=ArduinoApi(connection=connection)
except:
    print("Connexion impossible a l'arduino")

rpi = ArduinoApi()
rpi.pinMode(54, rpi.OUTPUT)
rpi.pinMode(55, rpi.OUTPUT)
rpi.pinMode(38, rpi.OUTPUT)
rpi.pinMode(3, rpi.INPUT)
rpi.pinMode(2, rpi.INPUT)
rpi.digitalWrite(38, rpi.LOW)
rpi.digitalWrite(55, rpi.HIGH)

pinMin = rpi.digitalRead(3)
while pinMin != 1:
    rpi.digitalWrite(54, rpi.HIGH)
    sleep(0.0001)
    rpi.digitalWrite(54, rpi.LOW)
    sleep(0.0001)
    pinMin = rpi.digitalRead(3)


#Désactivation du frein
rpi.digitalWrite(38, rpi.LOW)
rpi.digitalWrite(55, rpi.LOW)


for i in range(34000):
        rpi.digitalWrite(54, rpi.HIGH)
        sleep(0.0001)
        rpi.digitalWrite(54, rpi.LOW)
        sleep(0.0001)
    print("P5")


except:
    print("fin")
