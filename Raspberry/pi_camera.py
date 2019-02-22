from picamera import PiCamera
import time

class Camera():

    def __init__(self):
        self.camera = PiCamera()
        self.camera.vflip = True
        self.photo_name = 'test.jpg'

    def take_photo(self):
        self.camera.start_preview()
        self.camera.capture(self.photo_name)
        self.camera.stop_preview()

