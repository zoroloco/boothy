
PHOTOBOOTH

This project is my photobooth for my wedding. For about $200, you can create a fun photobooth. Python already has a very rich API that interfaces with the camera.

Required materials:
   - Raspberry Pi 2 or 3
   - 5-5.25v, 2.1-2.4 amp DC power adaptor for the Pi.
   - Raspberry Pi Camera module 
   - 7 inch LCD screen (https://www.element14.com/community/docs/DOC-78156/l/raspberry-pi-7-touchscreen-display)
   - Canon Selphy 1200 printer
   - Big huge red button (https://www.sparkfun.com/products/9181)
   - Stranded / Solid jumper wires
   - A23 12v alkaline battery
   - Soldering tools
   - Lots and lots of duct tape!

1.) Install the latest Raspbian distribution to your Raspberry Pi. This has been tested on Jessie.
2.) Follow the install steps from INSTALL.txt file.  This will give you the necessary libraries.
3.) Connect the LCD and camera to the Pi and plug it in.
4.) Plug in the printer with USB connection and setup your CUPs config file by enabling port 631 and add the printer by going to      yourrpihostname:631 on your browser.
    Use the following driver file: Canon SELPHY CP900 - CUPS+Gutenprint v5.2.10.  You can verify with test page print.
5.) Google how to disable the LCD from going to sleep on your rpi.  

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

Image of the front:
https://drive.google.com/file/d/0B7EyXq1CH6WfVTJGTGxhYlRDTFE/view?usp=drivesdk&resourcekey=0-B2UwrwTKijq_Vk6iMs2Xrw

Image of the inside:
https://drive.google.com/file/d/0B7EyXq1CH6WfaVoybW5hY0thRGs/view?usp=drivesdk&resourcekey=0-sNXYj3zFB9shJUTfyUbbNQ

