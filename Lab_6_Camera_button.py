from gpiozero import Button
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

button = Button(2)
button2 = Button(3)
camera = PiCamera()

def capture():
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/Documents/Programs/Lab_6/Lab_6_Camera_Button/%s.jpg' % timestamp)
    print('picture taken')
    
button.when_pressed = capture

def record():
    timestamp = datetime.now().isoformat()
    camera.resolution = (640,480)
    camera.start_recording('/home/pi/Documents/Programs/Lab_6/Lab_6_Camera_Button/%s.h264' % timestamp)
    camera.wait_recording(10)
    camera.stop_recording()
    
    print('recording finished')
    
button2.when_pressed = record

pause()