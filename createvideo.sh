#!/bin/sh

# Create video with:
#   * 2 images per second.
#   * Resolution of 720p.
#
SELFIE_DIRECTORY=$1
VIDEO_PATH=$2
ffmpeg -framerate 2 \
       -pattern_type glob -i "$SELFIE_DIRECTORY/"'*.jpg' \
       -c:v libx264 \
       -r 30 \
       -pix_fmt yuv420p \
       $VIDEO_PATH