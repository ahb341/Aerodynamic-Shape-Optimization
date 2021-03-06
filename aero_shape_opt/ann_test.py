import os
import numpy as np
from ann_2D.airfoil import Airfoil

# Change directory into folder of this script
os.chdir(os.path.dirname(__file__))

# Create standard airfoil object
af = Airfoil('mh32',0.3,2e5)
af.setXCoordsFromPath()
af.setYCoordsFromPath()
af.cleanAirfoil()

# print(af.x.shape)
# print(af.y.shape)
