#Y_moins.py 
pinStepY = 60
pinDirY = 61
pinEnableY = 56

from nanpy import (ArduinoApi, SerialManager)
from time import sleep

connection = SerialManager(device='/dev/ttyACM0')
rpi=ArduinoApi(connection=connection)

rpi.pinMode(pinStepY, rpi.OUTPUT)
rpi.pinMode(pinDirY, rpi.OUTPUT)
rpi.pinMode(pinEnableY, rpi.OUTPUT)

rpi.digitalWrite(pinEnableY, rpi.LOW)
rpi.digitalWrite(pinDirY, rpi.HIGH)

for i in range(250):
    rpi.digitalWrite(pinStepY, rpi.LOW)
    rpi.digitalWrite(pinStepY, rpi.HIGH)
