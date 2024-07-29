import RPi.GPIO as GPIO
import time

# Definir pino GPIO para o botão
BUTTON_PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def is_button_pressed():
    return GPIO.input(BUTTON_PIN) == GPIO.LOW

try:
    while True:
        if is_button_pressed():
            print("Botão pressionado!")
        else:
            print("Botão não pressionado!")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
    GPIO.cleanup()