import picamera
import itertools
import cups
import subprocess

from PIL import Image
from time import sleep

filePath = "/mnt/share/boothy/"
tempFilePath = "/tmp/"
IMAGE_WIDTH  = 640
IMAGE_HEIGHT = 480
fileName = "love_final.jpg"

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
                     tempFilePath+"0.jpg",
                     tempFilePath+"1.jpg",
                     tempFilePath+"2.jpg",
                     tempFilePath+"3.jpg",
                     "-geometry", "+2+2",
                     filePath+fileName])
    print "Images have been merged."

#adds a text decoration to the image.
def convertAddText(imageName):
    subprocess.call(["convert",
                "-font", "/usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf",
                "-pointsize", "40",
                "-fill", "HotPink2",
                "-draw", "text 0,0 \'Nadine & Kenneth\'",
                "-wave", "-50x640",
                imageName, imageName])
    print "Text overlay added to image "+imageName

def captureDummyImage(imageName):
    #create a dummy blank
    subprocess.call(["convert",
                     "-size", "640x480",
                     "xc:white",
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


captureImage(tempFilePath+"0.jpg")
sleep(1)
captureImage(tempFilePath+"1.jpg")
sleep(1)
captureImage(tempFilePath+"2.jpg")
sleep(1)
captureDummyImage(tempFilePath+"3.jpg")
sleep(2)
convertAddText(tempFilePath+"3.jpg")
convertMergeImages()
#printPic()
