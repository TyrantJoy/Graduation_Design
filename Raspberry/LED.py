import RPi.GPIO as GPIO

class ControlLED():
    
    def __init__(self):

        self.channel = 24
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.OUT)
    
    def closeLED(self):
        GPIO.output(self.channel, GPIO.LOW)

    def openLED(self):
        GPIO.output(self.channel, GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup()
