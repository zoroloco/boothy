import picamera
import itertools
import cups
import subprocess
import os
import sys
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont
from time import sleep

IMG1             = "1.jpg"
IMG2             = "2.jpg"
IMG3             = "3.jpg"
IMG4             = "4logo.png"
filePath         = ""
fileName         = "love_final.jpg"
IMAGE_WIDTH      = 640
IMAGE_HEIGHT     = 480
BUTTON_PIN       = 26
overlay_renderer = None
buttonEvent      = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#print the image
def printPic():
    addPreviewOverlay(435,335,100,"printing...")
    conn = cups.Connection()
    printers = conn.getPrinters()
    default_printer = printers.keys()[0]
    cups.setUser('pi')
    conn.printFile (default_printer, fileName, "boothy", {'fit-to-page':'True'})
    print "Print job successfully created."
    sleep(10)

#merges the 4 images
def convertMergeImages():
    addPreviewOverlay(335,335,100,"merging images...")
    #now merge all the images
    subprocess.call(["montage",
                     IMG1,IMG2,IMG3,IMG4,
                     "-geometry", "+2+2",
                     filePath+fileName])
    print "Images have been merged."

def cleanUp():
    print "Deleting any old images."
    if os.path.isfile(IMG1):
        os.remove(IMG1)
    if os.path.isfile(IMG2):
        os.remove(IMG2)
    if os.path.isfile(IMG3):
        os.remove(IMG3)
    if os.path.isfile(fileName):
        os.remove(fileName)

def countdownFrom(secondsStr):
    secondsNum = int(secondsStr)
    if secondsNum >= 0 :
        while secondsNum > 0 :
            addPreviewOverlay(635,215,200,str(secondsNum))
            sleep(1)
            secondsNum=secondsNum-1

def captureImage(imageName):
    addPreviewOverlay(535,335,100,"smile!")
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
    print "Starting play sequence"

    countdownFrom(5)
    captureImage(IMG1)
    sleep(1)

    countdownFrom(5)
    captureImage(IMG2)
    sleep(1)

    countdownFrom(5)
    captureImage(IMG3)
    sleep(1)

    convertMergeImages()
    sleep(1)
    #printPic()
    cleanUp()

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
        print "Starting preview"
        camera.start_preview()
        addPreviewOverlay(135,335,100,"Press red button to begin!")

        print "Starting app loop"
        while True:
            input_state = GPIO.input(BUTTON_PIN)
            if input_state == True :
                if buttonEvent == False :
                    buttonEvent = True
                    print "Big red button pressed!"
                    play()
                    addPreviewOverlay(135,335,100,"Press red button to begin!")
            else :
                if buttonEvent == True :
                    buttonEvent = False
                    print "Big red button de-pressed!"
    except:
        print 'Unexpected error : ', sys.exc_info()[0], sys.exc_info()[1]
    finally:
        camera.close()
