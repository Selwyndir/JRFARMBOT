#X_plus.py 
# Younes Dkhira
# Avance chariot X 5mm sens +
#
# Cablage PIN Arduino
pinStepX = 54
pinDirX = 55
pinEnableX = 38

from nanpy import (ArduinoApi, SerialManager)
from time import sleep

connection = SerialManager(device='/dev/ttyACM0')
rpi=ArduinoApi(connection=connection)

#Fin initialisation

#Declaration des entrees / sorties
rpi.pinMode(pinStepX, rpi.OUTPUT)
rpi.pinMode(pinDirX, rpi.OUTPUT)
rpi.pinMode(pinEnableX, rpi.OUTPUT)

#Desactivation du frein
rpi.digitalWrite(pinEnableX, rpi.LOW)

#Choix de la direction => Sens Positif
rpi.digitalWrite(pinDirX, rpi.LOW)

#Avance de 5mm sur X+ <=> 1 tour de MotX <=> 200 pas pour le moteur

for i in range(200):
    rpi.digitalWrite(pinStepX, rpi.LOW)
    rpi.digitalWrite(pinStepX, rpi.HIGH)
