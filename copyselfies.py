"""
Locates all close-up selfies in a directory, and copies them to another
directory.
"""

import detectface
import os
import argparse
import shutil
import multiprocessing


def main():
    """
    Entry point for the script.
    """

    # Process command-line arguments.
    args = handle_arguments()

    # Get paths to all images.
    image_paths = get_all_images(args.source, [".jpg"])

    # Process each image to see if it's a selfie.
    selfie_paths = get_all_selfies(list(image_paths))

    # Copy each image into a directory.
    copy_selfies(selfie_paths, args.destination)


def handle_arguments():
    """
    Processes command-line arguments.
    :return: Command-line arguments.
    """
    parser = argparse.ArgumentParser(description='Copy selfies into a directory.')
    parser.add_argument('source', type=str,
                        help='Base directory to search for selfies')
    parser.add_argument('destination', type=str,
                        help='Directory to copy selfies to')
    return parser.parse_args()


def get_all_images(base_directory, accepted_formats):
    """
    Returns paths to all images.
    :param base_directory: Base directory to search in.
    :param accepted_formats: Accepted image formats.
    :return: Generator for image paths.
    """
    for subdir, dirs, files in os.walk(base_directory):
        for file in files:
            name, extension = os.path.splitext(file)
            if extension.lower() in accepted_formats:
                yield os.path.join(subdir, file)


def get_all_selfies(image_paths):
    """
    Gets the path to all selfies.
    :param image_paths: Images to look at that may or may not be selfies.
    :return: Paths to all selfies.
    """

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for image_is_selfie, image_path in pool.map(is_selfie, image_paths):
        if image_is_selfie:
            yield image_path


def is_selfie(image_path):
    """
    Returns if it's a selfie, with the path.
    :return: If it's a selfie and the path.
    """
    image_is_selfie = detectface.is_selfie(image_path)
    print("[%s] %s" % (image_is_selfie, image_path))
    return image_is_selfie, image_path


def copy_selfies(selfie_paths, destination):
    """
    Copies the selfie to a directory.
    :param selfie_paths: Selfies to copy.
    :param destination: Directory name.
    """

    for selfie_path in selfie_paths:
        shutil.copy2(selfie_path, destination)


if __name__ == "__main__":
    main()
