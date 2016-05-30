-- HLR

Plug-in
   Turns on raspivid preview
   Show text that says 'hit red button'
Press Red button
   Count down 3-2-1
   Flash
   Save Image 1
   Sleep 3 seconds
   Countdown 3-2-1
   Flash
   Save Image 2
   Sleep 3 seconds
   Count down 3-2-1
   Flash
   Save Image 3
   Display on screen "processing..."
   Merge the 3 images with template
   Print image

   Go back to raspivid preview
   Show text that says 'hit red button'


Sample imagemagick scripts:

convert -font /usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf -pointsize 40 -fill HotPink2 -draw 'text 90,660 "Nadine & Kenneth - July 23rd, 2016 - Dreams Tulum - Mexico" ' /mnt/share/boothy/love_montage.jpg /mnt/share/boothy/love_final.jpg

convert -size 640x480 xc:white /mnt/share/boothy/3.jpg

montage /mnt/share/boothy/0.jpg /mnt/share/boothy/1.jpg /mnt/share/boothy/2.jpg /mnt/share/boothy/3.jpg -geometry +2+2 /mnt/share/boothy/love_montage.jpg
