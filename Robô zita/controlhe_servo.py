import RPI.GPIO as GPIO
import time

# Definir pino GPIO para o servo motor
SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz
pwm.start(0)

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        set_angle(0)
        time.sleep(2)
        set_angle(90)
        time.sleep(2)
        set_angle(180)
        time.sleep(2)
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
    pwm.stop()
    GPIO.cleanup()