from sensor_ultrasônico import distance
from controle_motores import forward, backward, stop
import RPi.GPIO as GPIO # type: ignore
import time

try:
    while True:
        dist = distance()
        print("Distância: {:.2f} cm".format(dist))
        if dist < 20:
            stop()
            backward()
            time.sleep(1)
            stop()
        else:
            forward()
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
    GPIO.cleanup()
