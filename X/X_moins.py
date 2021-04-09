#X_moins.py
#Toni De Almeida
# Recule chariot X 5mm sens -
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

#Declaration des entrées / sorties
rpi.pinMode(pinStepX, rpi.OUTPUT)
rpi.pinMode(pinDirX, rpi.OUTPUT)
rpi.pinMode(pinEnableX, rpi.OUTPUT)

#Desactivation du frein
rpi.digitalWrite(pinEnableX, rpi.LOW)

#Choix de la direction => Sens Negatif
rpi.digitalWrite(pinDirX, rpi.HIGH)

#Recule de 5mm sur X+ <=> 1 tour de MotX <=> 200 pas pour le moteur

for i in range(200):
    rpi.digitalWrite(pinStepX, rpi.HIGH)
    rpi.digitalWrite(pinStepX, rpi.LOW)
