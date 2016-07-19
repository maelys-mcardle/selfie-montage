Create Progress Video From Selfies
==================================

This project is a quick script to create a montage video from a 
series of selfies. This is broken into two steps.

1. Identify the selfies from a collection of photographs and 
   copy the selfies to a directory.
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

### Requirements

### Running the script
