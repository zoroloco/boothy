import picamera
import itertools
import cups
import subprocess
import os
import sys
from PIL import Image, ImageDraw, ImageFont
from time import sleep

IMG1             = "1.jpg"
IMG2             = "2.jpg"
IMG3             = "3.jpg"
IMG4             = "4logo.png"
filePath         = "/mnt/share/boothy/"
fileName         = "love_final.jpg"
IMAGE_WIDTH      = 640
IMAGE_HEIGHT     = 480
overlay_renderer = None

def printPic():
    conn = cups.Connection()
    printers = conn.getPrinters ()
    printer_name=printers.keys()[0]
    conn.printFile (printer_name, file, filePath+fileName, {})
    print filePath+fileName+" sent to printer."

#merges the 4 images
def convertMergeImages():
    #now merge all the images
    subprocess.call(["montage",
                     IMG1,IMG2,IMG3,IMG4,
                     "-geometry", "+2+2",
                     filePath+fileName])
    print "Images have been merged."

def cleanUp():
    print "Deleting temp images."
    os.remove(IMG1)
    os.remove(IMG2)
    os.remove(IMG3)

def captureImage(imageName):
    addPreviewOverlay(635,215,100,"3")
    sleep(1)
    addPreviewOverlay(636,215,100,"2")
    sleep(1)
    addPreviewOverlay(635,215,100,"1")
    sleep(1)
    addPreviewOverlay(635,335,75,"smile!")
    #save image
    camera.capture(imageName, resize=(IMAGE_WIDTH, IMAGE_HEIGHT))
    print "Image "+imageName+" captured."

def addPreviewOverlay(xcoord,ycoord,fontSize,overlayText):
    global overlay_renderer
    img = Image.new("RGB", (1280, 720))
    draw = ImageDraw.Draw(img)
    draw.font = ImageFont.truetype(
                    "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",fontSize)
    draw.text((xcoord,ycoord), overlayText, (247, 38, 206))

    if not overlay_renderer:
        overlay_renderer = camera.add_overlay(img.tostring(),
                                              layer=3,
                                              size=img.size,
                                              alpha=128);
    else:
        overlay_renderer.update(img.tostring())

#run a full series
def play():
    #captureImage(IMG1)
    #sleep(1)
    #captureImage(IMG2)
    #sleep(1)
    #captureImage(IMG3)
    #sleep(1)
    #convertMergeImages()
    printPic()
    #cleanUp()

#start flow
with picamera.PiCamera() as camera:
    #camera settings
    camera.resolution            = (1280, 720)
    camera.framerate             = 24
    camera.sharpness             = 0
    camera.contrast              = 0
    camera.brightness            = 50
    camera.saturation            = 0
    camera.ISO                   = 0
    camera.video_stabilization   = False
    camera.exposure_compensation = 0
    camera.exposure_mode         = 'auto'
    camera.meter_mode            = 'average'
    camera.awb_mode              = 'auto'
    camera.image_effect          = 'none'
    camera.color_effects         = None
    camera.rotation              = 0
    camera.hflip                 = False
    camera.vflip                 = False
    camera.crop                  = (0.0, 0.0, 1.0, 1.0)

    try:
        camera.start_preview()
        addPreviewOverlay(50,340,50,"WHATEVER YOU DO, DO NOT PRESS THE BIG RED BUTTON!!!")
        play()
    except:
        print 'Unexpected error : ', sys.exc_info()[0], sys.exc_info()[1]
    finally:
        camera.close()
