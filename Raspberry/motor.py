import RPi.GPIO as GPIO
import time

class Motor():

    def __init__(self):
        self.IN1 = 12
        self.IN2 = 16
        self.IN3 = 20
        self.IN4 = 21
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.OUT)      # Set pin's mode is output
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)

    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.IN1, w1)
        GPIO.output(self.IN2, w2)
        GPIO.output(self.IN3, w3)
        GPIO.output(self.IN4, w4)

    def stop(self):
        self.setStep(0, 0, 0, 0)

    def forward(self, delay, steps):
        self.stop()
        for i in range(0,steps):
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)

    def backward(self, delay, steps):
        self.stop()
        for i in range(0,steps):
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)

    def destroy(self):
        GPIO.cleanup()

