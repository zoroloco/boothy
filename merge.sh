#!/bin/sh

convert -size 640x480 xc:white /mnt/share/boothy/3.jpg
montage 0.jpg 1.jpg 2.jpg 3.jpg -geometry +2+2 /mnt/share/boothy/love_montage.jpg
