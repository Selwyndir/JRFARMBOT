#initialisation_X.py
# 2 = pinMaxX
# 3 = pinMinX
# 54 = pinStepX
# 55 = pinDirX
# 38 = pinEnableX
from nanpy import (ArduinoApi, SerialManager)
from time import *
i=0
try:
    connection = SerialManager()
    rpi=ArduinoApi(connection=connection)
except:
    print("Connexion impossibe à l'arduino")

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
    sleep(0.00005)
    rpi.digitalWrite(54, rpi.LOW)
    sleep(0.00005)
    pinMin = rpi.digitalRead(3)
