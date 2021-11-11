#Z_moins.py 
pinStepZ = 46
pinDirZ = 48
pinEnableZ = 62

from nanpy import (ArduinoApi, SerialManager)
from time import sleep

connection = SerialManager(device='/dev/ttyACM0')
rpi=ArduinoApi(connection=connection)

rpi.pinMode(pinStepZ, rpi.OUTPUT)
rpi.pinMode(pinDirZ, rpi.OUTPUT)
rpi.pinMode(pinEnableZ, rpi.OUTPUT)

rpi.digitalWrite(pinEnableZ, rpi.LOW)
rpi.digitalWrite(pinDirZ, rpi.HIGH)

for i in range(250):
    rpi.digitalWrite(pinStepZ, rpi.LOW)
    rpi.digitalWrite(pinStepZ, rpi.HIGH)
