import RPi.GPIO as GPIO
import time

# Definir pino GPIO para o LED
LED_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def led_on():
    GPIO.output(LED_PIN, True)

def led_off():
    GPIO.output(LED_PIN, False)

try:
    while True:
        led_on()
        time.sleep(1)
        led_off()
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
    GPIO.cleanup()