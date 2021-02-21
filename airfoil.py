import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

class Airfoil:
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
        return np.loadtxt(path,skiprows=1)

    def setXCoordsFromPath(self):
        df = self.load(self.path)
        self.x = df[:,0]

    def setYCoordsFromPath(self):
        df = self.load(self.path)
        self.y = df[:,1]

    def saveImg(self):
        img_file = '{}_img.png'.format(self.name)
        plt.savefig(img_file)
        return img_file

    def pixel_grid(self):
        # Given airfoil x and y coordinates and airfoil name, 
        # save a plot of the shaded airfoil, and return a
        # greyscale image matrix
        
        # Create plot of filled airfoil
        plt.fill(self.x,self.y,'k')
        plt.axis('equal')
        plt.axis('off')
        # plt.show()
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

