"""
Face detection module.
"""

import cv2


def is_selfie(image_path):
    """
    Indicates whether the image specified is a selfie.
    :param image_path: path to the image.
    :return: boolean indicating if its a selfie.
    """

    cascade_path = "cascade.xml"

    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Read the image
    image = cv2.imread(image_path)

    # Make the image smaller to fit 800 pixel width as a maximum,
    # and then gray scale, to speed up detection.
    img_width, img_height, colour_depth = image.shape
    new_width = 800
    new_height = int((float(new_width) / img_width) * img_height)
    image_shrunk = cv2.resize(image, (new_width, new_height))
    image_as_gray_scale = cv2.cvtColor(image_shrunk, cv2.COLOR_BGR2GRAY)

    # Face in a selfie should be at least a given proportion of the image.
    face_size_proportion = 3
    min_face_width = int(new_width/face_size_proportion)
    min_face_height = int(new_height/face_size_proportion)
    min_face_size = min(min_face_width, min_face_height)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        image_as_gray_scale,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(min_face_size, min_face_size),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Selfies should have one face.
    return len(faces) == 1
