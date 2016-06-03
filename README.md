
PHOTOBOOTH

This project is my photobooth for my wedding. For about $200, you can create a fun photobooth. Python already has a very rich API that interfaces with the camera.

Required materials:
   - Raspberry Pi 2
   - 2.1 amp DC power adaptor
   - Raspberry Pi Camera module (https://www.raspberrypi.org/products/camera-module/)
   - 7 inch LCD screen (https://www.element14.com/community/docs/DOC-78156/l/raspberry-pi-7-touchscreen-display)
   - Canon Selphy 1200 printer
   - Big huge red button (https://www.sparkfun.com/products/9181)

1.) Install the latest Raspbian distribution to your Raspberry Pi. This has been tested on Jessie.
2.) Follow the install steps from INSTALL.txt file.  This will give you the necessary libraries.
3.) Connect the LCD and camera to the Pi and plug it in.

Funcionality:
    Plug in the Raspberry Pi 2
    The LCD shows live video from the camera
    Press the red button
    You see countdown on the video screen
    First image taken
    Countdown again
    Second image taken
    Countdown again
    Final image taken
    Merge the 3 images to a pre-defined 4th image template
    Send new file to the printer
