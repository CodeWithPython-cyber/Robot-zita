import RPi.GPIO as GPIO
import time

SENSOR_PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(SENSOR_PIN) == GPIO.HIGH:
            print("Sensor detectou obstáculo!")
        else:
            print("Nenhum obstáculo detectado.")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
    GPIO.cleanup()