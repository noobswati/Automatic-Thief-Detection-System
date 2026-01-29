from picamera2 import Picamera2
from datetime import datetime
import time

def capture_image():
    cam = Picamera2()
    cam.start()
    time.sleep(2)

    filename = f"static/captured_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    cam.capture_file(filename)
    cam.stop()

    return filename
