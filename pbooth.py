import picamera
import itertools
import cups
import subprocess

from PIL import Image
from time import sleep

def printPic():
    conn = cups.Connection()
    printers = conn.getPrinters ()
    printer_name=printers.keys()[0]
    conn.printFile (printer_name, file, "test", {})

#merges the three images
def convertMergeImages():
    subprocess.call(["convert"])

#adds the text to final image.
def convertAddText():
    subprocess.call(["convert",
                "-font", "/usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf",
                "-pointsize", "40",
                "-fill", "HotPink2",
                "-draw" "'text 90,660 \"Nadine & Kenneth - July 23rd, 2016 - Dreams Tulum - Mexico\" '",
                "love.jpg", "love_final.jpg"])

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24

    try:
        camera.start_preview()

        index = 0;
        while index < 2:
            #save image
            camera.capture("temp"+'index'+".jpg",, resize=(320, 240)))
            index=index+1
            sleep(2)
        #printPic()
    finally:
        camera.close()

#convertMergeImages()
#convertText()
