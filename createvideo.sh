#!/bin/sh

SELFIE_DIRECTORY=$1
AUDIO_PATH=$2
VIDEO_PATH=$3

# Auto-rotate JPEG images whose rotation is stored in EXIF metadata.
find $SELFIE_DIRECTORY -name '*.jpg' -print | xargs exiftran -a -i

# Create video at 3 images per second.
ffmpeg -framerate 3 \
       -pattern_type glob -i "$SELFIE_DIRECTORY/"'*.jpg' \
       -i $AUDIO_PATH \
       -c:v libx264 \
       -r 30 \
       -pix_fmt yuv420p \
       -shortest \
       $VIDEO_PATH