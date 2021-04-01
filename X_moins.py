#X_moins.py 
#
# Recule chariot X 5mm sens -
#
# Cablage PIN Arduino
# 54 = pinStep 
# 55 = pinDir
# 38 = pinEnable
#
from nanpy import ArduinoApi
from time import *
i=0

try:
    connection = SerialManager()
    rpi=ArduinoApi(connection=connection)
except:
    print("Connexion impossible a l'arduino")

#Fin initialisation

#Déclaration des entrées / sorties
rpi.pinMode(54, rpi.OUTPUT)
rpi.pinMode(55, rpi.OUTPUT)
rpi.pinMode(38, rpi.OUTPUT)

#Désactivation du frein
rpi.digitalWrite(38, rpi.LOW)

#Choix de la direction => Sens Négatif
rpi.digitalWrite(55, rpi.HIGH)

#Recule de 5mm sur X+ <=> 1 tour de MotX <=> 200 pas pour le moteur

for i in range(200):
        rpi.digitalWrite(54, rpi.HIGH)
        sleep(0.0001)
        rpi.digitalWrite(54, rpi.LOW)
        sleep(0.0001)
    print("Fin des 200 pas => Recule de 5mm")


except:
    print("fin")
