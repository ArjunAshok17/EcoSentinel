"""
    This program defines the operations necessary for labeling landsat images right before they are fed into the 
    TensorFlow model for training.

    The operations relies on the channels in the images fed in, using purely the green value to estimate the amount of 
    ecological loss in the area. This can later be refined to account for Fall colors, deciduous vs coniferous forests, 
    etc. over time.
"""

from PIL import Image   # image manipulation
import numpy as np      # image array manipulation


# calculates amount of green ONLY #
def green_cover(img):
    # define variables #
    green_cov_cutoff = 100      # min value for a pixel to be considered a part of forest
    green_cov_sum = 0           # holds number of green pixels
    num_pixels = 0              # holds total number of pixels
    
    # convert to numpy array #
    if type(img) != "<class \'numpy.ndarray\'>":
        img = np.array(img, np.uint8)
    
        # # drop RB channels #
        # img[ :: , :: , 2] = 0
        # img[ :: , :: , 0] = 0

    # get green_cover #
    for row in img:
        for pixel in row:
            num_pixels += 1
            if (pixel[1] > green_cov_cutoff):
                green_cov_sum += 1
    
    # return percentage #
    num_pixels = img
    return float(green_cov_sum) / num_pixels
