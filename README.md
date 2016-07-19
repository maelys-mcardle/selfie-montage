Selfie Video Montage
====================

This project contains scripts to automate the process of creating 
a video montage of selfies. For instance, as seen in some progress
videos for trans folk.

This process is split into three steps:

1. Identify selfies from a collection of miscellaneous 
   photographs, then copy the selfies to a directory.
2. Manually review the selfies in a directory.
3. Create a montage video from the selfies.

Identify the selfies
--------------------

A python script `copyselfies.py` is available to identify selfies 
from a collection of photographs and copy them to a directory.
 
### Requirements

The script requires to have `Python 2.7` and the `opencv` library 
for Python installed. In Fedora, this can be installed with the 
following:

    sudo dnf install python opencv-python
    
The script assumes that photos are stored in the `.jpg` format.

### Running the script

Run the script the following way.

    ./copyselfies.py /path/for/photos /path/to/copy/selfies/to
    
The selfies will then be copied to the specified directory.

Manually review selfies
-----------------------

The script may have produced false positives. In this step the
photos thought to be selfies will have to be combed through, and
the false positives removed.

Create montage video
--------------------

A script called `createvideo.sh` is available to create videos
from the selfies.

### Requirements

`ffmpeg` and `exiftran` are required to run the script. They can be 
installed in Fedora by running the following command:

    sudo dnf install ffmpeg fbida

### Running the script

To create the video, run the following:

    ./createvideo.sh /path/to/selfies montage.mp4
    
The script will then create the `.mp4` video file with the 
montage.