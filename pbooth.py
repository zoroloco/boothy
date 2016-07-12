# boothy - Photobooth application for Raspberry Pi
# developed by Kenneth Centurion
#
# This application will take 3 images with PHOTO_DELAY seconds between.
# Will have text overlay on the screen with a countdown.  Will then merge
# the 3 images with a template fourth image "4logo.png" in a grid. The final
# image is then sent to the printer using the CUPs API.

import picamera
import itertools
import cups
import subprocess
import os
from shutil import copyfile
import sys
import time
import logging
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

IMG1             = "1.jpg"
IMG2             = "2.jpg"
IMG3             = "3.jpg"
CurrentWorkingDir= "/usr/local/src/boothy"
IMG4             = "4logo.png"
logDir           = "logs"
archiveDir       = "photos"
IMAGE_WIDTH      = 640
IMAGE_HEIGHT     = 480
BUTTON_PIN       = 26
LED_PIN          = 19 #connected to external 12v.
PHOTO_DELAY      = 7
overlay_renderer = None
buttonEvent      = False

#setup GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

#print the image
def printPic(fileName):
    addPreviewOverlay(435,335,100,"printing...")
    conn = cups.Connection()
    printers = conn.getPrinters()
    default_printer = printers.keys()[0]
    cups.setUser('pi')
    conn.printFile (default_printer, fileName, "boothy", {'fit-to-page':'True'})
    logging.info("Print job successfully created.");
    time.sleep(10)

#merges the 4 images
def convertMergeImages(fileName):
    addPreviewOverlay(335,335,100,"merging images...")
    #now merge all the images
    subprocess.call(["montage",
                     IMG1,IMG2,IMG3,IMG4,
                     "-geometry", "+2+2",
                     fileName])
    logging.info("Images have been merged.")

def deleteImages(fileName):
    logging.info("Deleting any old images.")
    if os.path.isfile(IMG1):
        os.remove(IMG1)
    if os.path.isfile(IMG2):
        os.remove(IMG2)
    if os.path.isfile(IMG3):
        os.remove(IMG3)
    if os.path.isfile(fileName):
        os.remove(fileName);

def cleanUp():
    GPIO.cleanup()

def archiveImage(fileName):
    logging.info("Saving off image: "+fileName)
    copyfile(fileName,archiveDir+"/"+fileName)

def countdownFrom(secondsStr):
    secondsNum = int(secondsStr)
    if secondsNum >= 0 :
        while secondsNum > 0 :
            addPreviewOverlay(635,215,200,str(secondsNum))
            time.sleep(1)
            secondsNum=secondsNum-1

def captureImage(imageName):
    addPreviewOverlay(535,335,100,"smile!")
    #save image
    camera.capture(imageName, resize=(IMAGE_WIDTH, IMAGE_HEIGHT))
    logging.info("Image "+imageName+" captured.")

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

    fileName = time.strftime("%Y%m%d-%H%M%S")+".jpg"
    print "Created filename: "+fileName

    countdownFrom(PHOTO_DELAY)
    captureImage(IMG1)
    time.sleep(1)

    countdownFrom(PHOTO_DELAY)
    captureImage(IMG2)
    time.sleep(1)

    countdownFrom(PHOTO_DELAY)
    captureImage(IMG3)
    time.sleep(1)

    convertMergeImages(fileName)
    time.sleep(1)
    #printPic(fileName)

    archiveImage(fileName)
    deleteImages(fileName)

def initCamera(camera):
    logging.info("Initializing camera.")
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

def initLogger(output_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # create error file handler and set level to error
    handler = logging.FileHandler(output_dir+"/"+time.strftime("%Y%m%d")+"_error.log","w", encoding=None, delay="true")
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # create debug file handler and set level to debug
    handler = logging.FileHandler(output_dir+"/"+time.strftime("%Y%m%d")+"_debug.log","w", encoding=None, delay="true")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def onButtonPress():
    logging.info("Big red button pressed!")

    #turn on flash
    GPIO.output(LED_PIN,GPIO.HIGH)

    play()

    #turn off flash

    #reset the initial welcome message
    addPreviewOverlay(135,335,100,"Press red button to begin!")

def onButtonDePress():
    logging.info("Big red button de-pressed!")

#start flow
with picamera.PiCamera() as camera:
    os.chdir(CurrentWorkingDir)

    try:
        initLogger(logDir)
        initCamera(camera)
        GPIO.output(LED_PIN,GPIO.LOW)
        logging.info("Starting preview")
        camera.start_preview()
        addPreviewOverlay(135,335,100,"Press red button to begin!")

        logging.info("Starting application loop")
        while True:
            input_state = GPIO.input(BUTTON_PIN)
            if input_state == True :
                if buttonEvent == False :
                    buttonEvent = True
                    onButtonPress()
            else :
                if buttonEvent == True :
                    buttonEvent = False
                    onButtonDePress()
    except BaseException:
        logging.error("Unhandled exception : " , exc_info=True)
        camera.close()
        cleanUp()
    finally:
        logging.info("quitting...")
        cleanUp()
        camera.close()

#end
