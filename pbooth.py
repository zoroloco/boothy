import picamera
import itertools
import cups
import subprocess

from PIL import Image
from time import sleep

IMG1         = "1.jpg"
IMG2         = "2.jpg"
IMG3         = "3.jpg"
IMG4         = "4logo.png"
filePath     = "/mnt/share/boothy/"
fileName     = "love_final.jpg"
IMAGE_WIDTH  = 640
IMAGE_HEIGHT = 480

def printPic():
    conn = cups.Connection()
    printers = conn.getPrinters ()
    printer_name=printers.keys()[0]
    conn.printFile (printer_name, file, filePath+"love_montage.jpg", {})
    print filePath+fileName+" sent to printer."

#merges the three images
def convertMergeImages(img1,img2,img3,img4):
    #now merge all the images
    subprocess.call(["montage",
                     img1,img2,img3,img4,
                     "-geometry", "+2+2",
                     filePath+fileName])
    print "Images have been merged."

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


captureImage(IMG1)
sleep(1)
captureImage(IMG2)
sleep(1)
captureImage(IMG3)
sleep(1)
convertMergeImages(IMG1,IMG2,IMG3,IMG4)
#printPic()
