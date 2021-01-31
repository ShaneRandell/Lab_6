from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024,768)
camera.start_preview()

sleep(2)
camera.capture('test_photo.jpg')

sleep(2)

camera.resolution = (640,480)
camera.start_recording('test_video.h264')
camera.wait_recording(10)
camera.stop_recording()

print('finished recording')