import picamera
import time
import itertools
import cups

from PIL import Image
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24

    try:
        camera.start_preview()
        #time.sleep(10)
        #camera.stop_preview()
    finally:
        camera.close()

    #save image
    camera.capture('love.jpg')

    subprocess.call(['convert -font /usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf -pointsize 40 -fill HotPink2 -draw \'text 90,660 \\"Nadine & Kenneth - July 23rd, 2016 - Dreams Tulum - Mexico\\" \' love.jpg love1.jpg
'])

    #print
    #conn = cups.Connection()
    #printers = conn.getPrinters ()
    #printer_name=printers.keys()[0]
    #conn.printFile (printer_name, file, "test", {})
