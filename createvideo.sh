#!/bin/sh

SELFIE_DIRECTORY=$1
VIDEO_PATH=$2

# Auto-rotate JPEG images whose rotation is stored in EXIF metadata.
find $SELFIE_DIRECTORY -name '*.jpg' -print | xargs exiftran -a -i

# Create video at 2 images per second.
ffmpeg -framerate 2 \
       -pattern_type glob -i "$SELFIE_DIRECTORY/"'*.jpg' \
       -c:v libx264 \
       -r 30 \
       -pix_fmt yuv420p \
       $VIDEO_PATH