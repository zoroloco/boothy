import picamera
import itertools
import cups
import subprocess

from PIL import Image
from time import sleep

filePath = "/mnt/share/boothy/"
IMAGE_WIDTH  = 640
IMAGE_HEIGHT = 480

def printPic():
    conn = cups.Connection()
    printers = conn.getPrinters ()
    printer_name=printers.keys()[0]
    conn.printFile (printer_name, file, "test", {})

#merges the three images
def convertMergeImages():
    #create a dummy blank
    subprocess.call(["convert -size 640x480 xc:white /mnt/share/boothy/3.jpg"])
    #now check in a loop if the 3.jpg file exists. if so, then
    sleep(2)
    #now merge all the images
    subprocess.call(["montage 0.jpg 1.jpg 2.jpg 3.jpg -geometry +2+2 /mnt/share/boothy/love_montage.jpg"])

#adds the text to final image.
def convertAddText():
    subprocess.call(["convert",
                "-font", "/usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf",
                "-pointsize", "40",
                "-fill", "HotPink2",
                "-draw" "'text 90,660 \"Nadine & Kenneth - July 23rd, 2016 - Dreams Tulum - Mexico\" '",
                "love.jpg", "love_final.jpg"])

def captureImage(imageName):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.framerate = 24

        try:
            camera.start_preview()
            #save image
            camera.capture(imageName, resize=(IMAGE_WIDTH, IMAGE_HEIGHT))
        finally:
            camera.close()

captureImage(filePath+"0.jpg")
sleep(1)
captureImage(filePath+"1.jpg")
sleep(1)
captureImage(filePath+"2.jpg")
sleep(1)
convertMergeImages()
sleep(2)
convertAddText()
#printPic()
