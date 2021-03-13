#!/bin/sh

# To change the permissions of this file so it can be run in terminal, do
# chmod 755 make_email_images.sh

# To run, cd to the appropriate folder (note- that same folder will be where the image is saved) and run either:
# ./make_email_images.sh
# ./src/make_email_images.sh
# depending on which directory you currently are in

SAVETOFILENAME=email-address-image.png

echo Saving email addresses as an image. May take a second.

echo "Rahul Yerrabelli: \n 1. ryerrabelli@gmail.com \n 2. rsy2@illinois.edu \n 3. ryerrab1@alumni.jh.edu" | convert -background none -density 400 -resample 150 -unsharp 0x.5 -font "arial" text:- -trim +repage -bordercolor white -border 0 $SAVETOFILENAME

echo Done. Saved to file name $SAVETOFILENAME.