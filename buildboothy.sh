#!/bin/bash
# Instruction: move this file to /usr/local/src and run from there.
#
# chmod +x build.sh
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
