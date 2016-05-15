#!/bin/sh

convert -size 640x480 xc:white /mnt/share/boothy/3.jpg
montage /mnt/share/boothy/0.jpg /mnt/share/boothy/1.jpg /mnt/share/boothy/2.jpg /mnt/share/boothy/3.jpg -geometry +2+2 /mnt/share/boothy/love_montage.jpg
