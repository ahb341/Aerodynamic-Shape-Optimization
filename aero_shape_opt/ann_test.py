import os
import numpy as np
from matplotlib import pyplot as plt

from ann_2D.airfoil import Airfoil
from ann_2D.ANN import run_ANN

# Change directory into folder of this script
os.chdir(os.path.dirname(__file__))

# Create standard airfoil object
af = Airfoil('mh32',0.3,2e5)
af.setXCoordsFromPath()
af.setYCoordsFromPath()
af.cleanAirfoil()

# Plot airfoil shape
plt.plot(af.x,af.y,'-.')
plt.plot(af.interp_x,af.interp_y,'-.')
plt.show()

# Call neural network
run_ANN(af)

