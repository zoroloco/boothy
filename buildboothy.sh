#!/bin/bash
# Instruction: move this file to /usr/local/src and run from there.
#
# chmod +x buildboothy.sh
#
# This script will get latest site from github
#
clear

echo "Running build script."

SRC_DIR="/usr/local/src/boothy"

echo "Deleting source directory"
rm -rf $SRC_DIR

echo "Creating source directory"
mkdir $SRC_DIR

echo "Retrieving latest repo: git clone https://github.com/zoroloco/boothy.git " $SRC_DIR
git clone https://github.com/zoroloco/boothy.git $SRC_DIR

echo "Making run file executable."
chmod +x $SRC_DIR/run.sh

chmod +x $SRC_DIR/buildboothy.sh

echo "Making link to desktop for saved images."
mkdir /home/pi/Desktop/fotos
ln -s $SRC_DIR/photos /home/pi/Desktop

echo "Making startup script executable"
chmod +x $SRC_DIR/rpi/etc/init.d/boothyStart.sh
echo "Moving startup script to /etc/init.d"
cp $SRC_DIR/rpi/etc/init.d/boothyStart.sh /etc/init.d
echo "Making boothy run automatically at boot"
update-rc.d boothyStart.sh defaults
