import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import os

class Airfoil:

    AF_PATH = 'aero_shape_opt\\datasets\\airfoils'

    # Inputs
        # M: Mach Number
        # Re: Reynolds Number
    # Properties
        # xcoords: x coordinates of airfoil
        # ycoords: y coordinates of airfoil
    def __init__(self, name, M, Re):
        self.name = name
        self.path = '{0}\\{1}.dat'.format(self.AF_PATH,name)
        self.M = M
        self.Re = Re
        self.x = []
        self.y = []

        self.setCoordsFromPath()
        # af.setXCoordsFromPath()
        # af.setYCoordsFromPath()

    def load(self, path):
        return np.loadtxt(path,skiprows=1)

    def setCoordsFromPath(self):
        df = self.load(self.path)
        self.x = df[:,0]
        self.y = df[:,1]

    # def setXCoordsFromPath(self):
    #     df = self.load(self.path)
    #     self.x = df[:,0]

    # def setYCoordsFromPath(self):
    #     df = self.load(self.path)
    #     self.y = df[:,1]

    def saveImg(self):
        # Given airfoil x and y coordinates and airfoil name, 
        # save a plot of the shaded airfoil, and return a
        # greyscale image matrix
        # Create plot of filled airfoil
        IMG_SIZE = 64
        my_dpi = 22#10
        # plt.figure(figsize=(IMG_SIZE/my_dpi, IMG_SIZE/my_dpi/5.0), dpi=my_dpi)
        plt.figure(figsize=(IMG_SIZE/10, IMG_SIZE/10/5.0), dpi=my_dpi)
        plt.fill(self.x,self.y,'k')
        # plt.axis('equal')
        plt.axis('off')
        # plt.show()
        img_file = '{}_img.png'.format(self.name)
        plt.savefig(img_file,dpi=my_dpi)
        plt.close()
        return img_file

    def pixel_grid(self):
        img_file = self.saveImg()

        # Read in pixel values in greyscale
        image = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)
        pixels = image/255 # scale down to range [0, 1]

        os.remove('{}_img.png'.format(self.name))

        return pixels

    # def f(self, x):
    #     return np.sin(x)
    
    # def test(self):
    #     x = np.linspace(-3,3,1000)
    #     plt.plot(x,self.f(x))
    #     plt.show()

