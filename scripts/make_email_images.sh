#!/bin/sh

# To change the permissions of this file so it can be run in terminal, do
# chmod 755 make_email_images.sh

# To run, cd to the main project folder and run:
# ./scripts/make_email_images.sh
# Alternatively, if change the SAVETOFILENAME to "../docs/email-address-image.png", you can go to the subfolder and do:
# # ./make_email_images.sh
#

# SAVETOFILENAME can be passed in; otherwise, default value will be used
SAVETOFILENAME=${1:-"docs/email-address-image.png"}
# https://linuxhandbook.com/bash-arguments/

echo Saving email addresses as an image. May take a second.

echo "Rahul Yerrabelli: \n 1. ryerrabelli@gmail.com \n 2. rsy2@illinois.edu \n 3. ryerrab1@alumni.jh.edu" | convert -background none -density 400 -resample 150 -unsharp 0x.5 -font "arial" text:- -trim +repage -bordercolor white -border 0 $SAVETOFILENAME

echo Done. Saved to file name $SAVETOFILENAME.