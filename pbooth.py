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
    #create a dummy blank
    subprocess.call(["convert",
                     "-size", "640x480",
                     "xc:white",
                     tempFilePath+"3.jpg"])
    #now check in a loop if the 3.jpg file exists. if so, then
    sleep(2)
    #now merge all the images
    print "Blank 4th image created."
    subprocess.call(["montage",
                     tempFilePath+"0.jpg",
                     tempFilePath+"1.jpg",
                     tempFilePath+"2.jpg",
                     tempFilePath+"3.jpg",
                     "-geometry", "+2+2",
                     tempFilePath+"love_montage.jpg"])
    print "Images have been merged."

#adds the text to final image.
def convertAddText():
    subprocess.call(["convert",
                "-font", "/usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf",
                "-pointsize", "40",
                "-fill", "HotPink2",
                "-draw", "text 90,660 \'Nadine & Kenneth - July 23rd, 2016 - Dreams Tulum - Mexico\'",
                tempFilePath+"love_montage.jpg", filePath+fileName])
    print "Text overlay added to image."

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
convertMergeImages()
sleep(2)
convertAddText()
#printPic()
