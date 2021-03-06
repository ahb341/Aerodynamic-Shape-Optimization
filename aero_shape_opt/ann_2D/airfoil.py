import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
from scipy import interpolate


class Airfoil:
    
    # A constant representing the standard number of airfoil coord pts
    N_PTS_AIRFOIL = 100

    # Inputs
        # M: Mach Number
        # Re: Reynolds Number
    # Properties
        # xcoords: x coordinates of airfoil
        # ycoords: y coordinates of airfoil
    def __init__(self, name, M, Re):
        self.name = name
        self.path = '{}.dat'.format(name)
        self.M = M
        self.Re = Re
        self.x = []
        self.y = []

    def load(self, path):
        dat_folder = 'datasets\\airfoils\\'
        return np.loadtxt(dat_folder + path,skiprows=1)

    def setXCoordsFromPath(self):
        df = self.load(self.path)
        self.x = df[:,0]

    def setYCoordsFromPath(self):
        df = self.load(self.path)
        self.y = df[:,1]

    def cleanAirfoil(self):
        # Modifies airfoil
        print('Cleaning')
        tck, u = interpolate.splprep([self.x, self.y], k=3, s=0.0)
        t = np.linspace(0,1,self.N_PTS_AIRFOIL)
        interp_coords = interpolate.splev(t, tck) # evaluate at points
        self.interp_x = interp_coords[0]
        self.interp_y = interp_coords[1]
    

    def saveImg(self):
        # Given airfoil x and y coordinates and airfoil name, 
        # save a plot of the shaded airfoil, and return a
        # greyscale image matrix
        # Create plot of filled airfoil
        IMG_SIZE = 64
        my_dpi = 10
        plt.figure(figsize=(IMG_SIZE/my_dpi, IMG_SIZE/my_dpi), dpi=my_dpi)
        plt.fill(self.x,self.y,'k')
        plt.axis('equal')
        plt.axis('off')
        #plt.show()
        img_file = '{}_img.png'.format(self.name)
        plt.savefig(img_file,dpi=my_dpi)
        return img_file

    def pixel_grid(self):
        img_file = self.saveImg()

        # Read in pixel values in greyscale
        image = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)
        pixels = image/255 # scale down to range [0, 1]

        return pixels

    # def f(self, x):
    #     return np.sin(x)
    
    # def test(self):
    #     x = np.linspace(-3,3,1000)
    #     plt.plot(x,self.f(x))
    #     plt.show()

