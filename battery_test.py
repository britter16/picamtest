from datetime import datetime
import time
import RPi.GPIO as GPIO  # using Rpi.GPIO module
from time import sleep  # import function sleep for delay
import sys

GPIO.setmode(GPIO.BCM)  # GPIO numbering
GPIO.setwarnings(False)  # enable warning from GPIO
AN2 = 13  # set pwm2 pin on MD10-Hat
AN1 = 12  # set pwm1 pin on MD10-hat
DIG2 = 24  # set dir2 pin on MD10-Hat
DIG1 = 26  # set dir1 pin on MD10-Hat
GPIO.setup(AN2, GPIO.OUT)  # set pin as output
GPIO.setup(AN1, GPIO.OUT)  # set pin as output
GPIO.setup(DIG2, GPIO.OUT)  # set pin as output
GPIO.setup(DIG1, GPIO.OUT)  # set pin as output
sleep(1)  # delay for 1 seconds
p1 = GPIO.PWM(DIG1, 100)  # set pwm for M1
p2 = GPIO.PWM(DIG2, 100)  # set pwm for M2

if __name__ == "__main__":
    while 1:
        with open('test.txt', 'a') as file:
            file.write(str(datetime.now()) + "\n")
        file.close()

        GPIO.output(AN1, GPIO.HIGH)  # set AN1 as HIGH, M1B will turn ON
        GPIO.output(AN2, GPIO.HIGH)  # set AN2 as HIGH, M2B will turn ON
        p1.start(0)  # set Direction for M1
        p2.start(0)  # set Direction for M2
        sleep(0.2)  # delay for 2 second

        GPIO.output(AN1, GPIO.LOW)  # set AN1 as LOW, M1B will STOP
        sleep(0.2)
        GPIO.output(AN2, GPIO.LOW)  # set AN2 as HIGH, M2B will STOP
        p1.start(0)  # Direction can ignore
        p2.start(0)  # Direction can ignore

        GPIO.output(AN1, GPIO.HIGH)  # set AN1 as HIGH, M1B will turn ON
        GPIO.output(AN2, GPIO.HIGH)  # set AN2 as HIGH, M2B will turn ON
        p1.start(100)  # set Direction for M1
        p2.start(100)  # set Direction for M2
        sleep(0.2)  # delay for 2 second

        GPIO.output(AN1, GPIO.LOW)  # set AN1 as LOW, M1B will STOP
        sleep(0.2)
        GPIO.output(AN2, GPIO.LOW)  # set AN2 as HIGH, M2B will STOP
        p1.start(0)  # Direction can ignore
        p2.start(0)  # Direction can ignore

        time.sleep(300)
