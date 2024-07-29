import RPi.GPIO as GPIO
import time

# Definir pinos GPIO para os motores
MOTOR1A = 17
MOTOR1B = 18
MOTOR2A = 22
MOTOR2B = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR1A, GPIO.OUT)
GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR2A, GPIO.OUT)
GPIO.setup(MOTOR2B, GPIO.OUT)

def move_forward():
    GPIO.output(MOTOR1A, True)
    GPIO.output(MOTOR1B, False)
    GPIO.output(MOTOR2A, True)
    GPIO.output(MOTOR2B, False)

def move_backward():
    GPIO.output(MOTOR1A, False)
    GPIO.output(MOTOR1B, True)
    GPIO.output(MOTOR2A, False)
    GPIO.output(MOTOR2B, True)

def stop_motors():
    GPIO.output(MOTOR1A, False)
    GPIO.output(MOTOR1B, False)
    GPIO.output(MOTOR2A, False)
    GPIO.output(MOTOR2B, False)

def rotate_left():
    GPIO.output(MOTOR1A, False)
    GPIO.output(MOTOR1B, True)
    GPIO.output(MOTOR2A, True)
    GPIO.output(MOTOR2B, False)

def rotate_right():
    GPIO.output(MOTOR1A, True)
    GPIO.output(MOTOR1B, False)
    GPIO.output(MOTOR2A, False)
    GPIO.output(MOTOR2B, True)

try:
    while True:
        move_forward()
        time.sleep(2)
        stop_motors()
        time.sleep(1)
        move_backward()
        time.sleep(2)
        stop_motors()
        time.sleep(1)
        rotate_left()
        time.sleep(2)
        stop_motors()
        time.sleep(1)
        rotate_right()
        time.sleep(2)
        stop_motors()
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
    GPIO.cleanup()