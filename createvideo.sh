#!/bin/sh

# Create video with:
#   * 2 images per second.
#   * Resolution of 720p.
#
SELFIE_DIRECTORY=$1
VIDEO_PATH=$2
ffmpeg -r 2 -i $SELFIE_DIRECTORY/* -vf scale=-1:720 -c:v libx264 -crf 18 -preset veryslow -c:a copy $VIDEO_PATH