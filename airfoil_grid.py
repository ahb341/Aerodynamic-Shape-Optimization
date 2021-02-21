import os
import numpy as np
import matplotlib.pyplot as plt
import cv2


def pixel_grid(airfoil_x, airfoil_y, airfoil_name):
    # Given airfoil x and y coordinates and airfoil name, 
    # save a plot of the shaded airfoil, and return a
    # greyscale image matrix
    
    # Create plot of filled airfoil
    plt.fill(airfoil_x,airfoil_y,'k')
    plt.axis('equal')
    plt.axis('off')
    # plt.show()
    img_file = '{}_img.png'.format(airfoil_name)
    plt.savefig(img_file)

    # Read in pixel values in greyscale
    image = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)
    pixels = image/255 # scale down to range [0, 1]

    return pixels


# Airfoil
airfoil_name = 'mh32'

# Get airfoil coordinates
data = np.loadtxt('{}.dat'.format(airfoil_name),skiprows=1)
airfoil_x = data[:,0]
airfoil_y = data[:,1]

# Get grid and save image
pixels = pixel_grid(airfoil_x,airfoil_y,airfoil_name)

print(pixels)