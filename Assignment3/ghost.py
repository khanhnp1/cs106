"""
File: ghost.py
--------------
YOUR DESCRIPTION HERE
"""

import os
import sys

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    This Doctest creates a simple green image and tests against
    a pixel of RGB values (0, 0, 255)
    >>> green_im = SimpleImage.blank(20, 20, 'green')
    >>> green_pixel = green_im.get_pixel(0, 0)
    >>> get_pixel_dist(green_pixel, 0, 255, 0)
    0
    >>> get_pixel_dist(green_pixel, 0, 255, 255)
    65025
    >>> get_pixel_dist(green_pixel, 5, 255, 10)
    125
    """
    return (pixel.red - red)**2 + (pixel.green - green)**2 + (pixel.blue - blue)**2


def get_best_pixel(pixel_list):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across
    all pixels.

    Input:
        a list of pixels to be averaged and compared.  You can assume this list is never empty
    Returns:
        best (Pixel): pixel closest to RGB averages

    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    >>> best1.red, best1.green, best1.blue
    (0, 0, 255)
    >>> best2 = get_best_pixel([green_pixel, green_pixel, blue_pixel])
    >>> best2.red, best2.green, best2.blue
    (0, 255, 0)
    >>> best3 = get_best_pixel([red_pixel, red_pixel, red_pixel])
    >>> best3.red, best3.green, best3.blue
    (255, 0, 0)
    """
    average_red = 0
    average_green = 0
    average_blue = 0
    closet_pixel  = []
    distance = (255 ** 2) * 3
    for pixel in pixel_list:
        average_red   =  average_red   + pixel.red
        average_green =  average_green + pixel.green
        average_blue  =  average_blue  + pixel.blue

    average_red =  average_red // len(pixel_list)
    average_green =  average_green // len(pixel_list)
    average_blue =  average_blue // len(pixel_list)

    for pixel in pixel_list:
        dist = get_pixel_dist(pixel,  average_red,  average_green,  average_blue)
        if (dist < distance):
            distance = dist
            closet_pixel = pixel
    
    return closet_pixel


def create_ghost(image_list):
    """
    Given a list of image objects, this function creates and returns a Ghost
    solution image based on the images passed in. All the images passed
    in will be the same size.

    Input:
        a list images to be processed.  You can assume this list is never empty.
    Returns:
        a new Ghost solution image
    """
    pixel_list = []
    ghost_image = SimpleImage.blank(image_list[0].width, image_list[0].height)

    for pixel in ghost_image:
        pixel_list.clear()
        for image in image_list:
            pixel_list.append(image.get_pixel(pixel.x, pixel.y))         
        ghost_image.set_pixel(pixel.x, pixel.y, get_best_pixel(pixel_list))

    return ghost_image

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########
def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(directory, filename))
    return filenames

def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]

    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images)
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")


if __name__ == '__main__':
    main()
