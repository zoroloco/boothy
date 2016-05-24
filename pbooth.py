import picamera
import itertools
import cups
import subprocess

from PIL import Image
from time import sleep

filePath     = "/mnt/share/boothy/"
IMAGE_WIDTH  = 640
IMAGE_HEIGHT = 480
fileName     = "love_final.jpg"

def printPic():
    conn = cups.Connection()
    printers = conn.getPrinters ()
    printer_name=printers.keys()[0]
    conn.printFile (printer_name, file, filePath+"love_montage.jpg", {})
    print filePath+fileName+" sent to printer."

#merges the three images
def convertMergeImages():
    #now merge all the images
    subprocess.call(["montage",
                     filePath+"0.jpg",
                     filePath+"1.jpg",
                     filePath+"2.jpg",
                     filePath+"3.jpg",
                     "-geometry", "+2+2",
                     filePath+fileName])
    print "Images have been merged."

def captureDummyImage(imageName):
    #create a dummy blank
    subprocess.call(["convert",
                     "-size", "640x480",
                     "-font", "/usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf",
                     "-pointsize", "22",
                     "-fill", "HotPink2",
                     "label:\"Nadine & Kenneth - July 23, 2016 - Dreams Tulum, Mexico\"",
                     "-virtual-pixel", "background",
                     "-distort", "Arc 340",
                     imageName])

    print "Image "+imageName+" created."

def captureImage(imageName):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.framerate = 24

        try:
            camera.start_preview()
            #save image
            camera.capture(imageName, resize=(IMAGE_WIDTH, IMAGE_HEIGHT))
            print "Image "+imageName+" captured."
        finally:
            camera.close()


#captureImage(tempFilePath+"0.jpg")
#sleep(1)
#captureImage(tempFilePath+"1.jpg")
#sleep(1)
#captureImage(tempFilePath+"2.jpg")
#sleep(1)
captureDummyImage(filePath+"3.jpg")
#sleep(2)
#convertMergeImages()
#printPic()
