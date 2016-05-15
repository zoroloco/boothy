mport picamera
import time
import itertools
import cups
import threading
import subprocess

from PIL import Image
from time import sleep

class overlayText(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        subprocess.call(["convert",
                         "-font", "/usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf",
                         "-pointsize", "40",
                         "-fill", "HotPink2",
                         "-draw" "'text 90,660 \"Nadine & Kenneth - July 23rd, 2016 - Dreams Tulum - Mexico\" '",
                         "temp"+'threadID'+".jpg", 'threadID'+".jpg"])

def printPic():
    conn = cups.Connection()
    printers = conn.getPrinters ()
    printer_name=printers.keys()[0]
    conn.printFile (printer_name, file, "test", {})


with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24

    try:
        camera.start_preview()

        index = 0;
        while index < 2:
            #save image
            camera.capture("temp"+'index'+".jpg")
            overlayTextThread = overlayText(index)
            overlayTextThread.start()
            index=index+1
            time.sleep(1)

        #printPic()
    finally:
        camera.close()
