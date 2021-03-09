# Compress airfoil data into a single .npz folder for easier extraction later

import os
import numpy as np
import re
import warnings
import shutil
from cnn_2D.airfoil import Airfoil


airfoil_names = []
in_dir = "aero_shape_opt\\datasets\\airfoils"
out_dir = "aero_shape_opt\\datasets\\xfoil_data"

# Get list of airfoil names
for filename in os.listdir(in_dir):
    if filename.endswith(".dat"):
        name = filename[0:filename.find('.')]
        airfoil_names.append(name)

airfoil_inputs = []
airfoil_outputs = []

# Get airfoil information
for a_name in airfoil_names:
    coord_name = a_name + "_airfoil.txt"
    polar_name = a_name + "_polar.txt"
    
    try:
        # Coordinates. Turn off empty file warnings, since is caught
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            coords = np.loadtxt(out_dir + "\\" + coord_name)

        # Extract all polar data
        f = open(out_dir + "\\" + polar_name, 'r')
        xdata = f.read()
        f.close()
        xdata = xdata.splitlines()

        # Extract [Mach no., Reynold n., Ncrit]
        header_nums = re.findall(r'[-+]?\d+\.*\d*[ e ]*\d*', xdata[8])
        header_nums = [float(a.replace(" ","")) for a in header_nums]    
        Ma = header_nums[0]
        Re = header_nums[1] 
    except:
        print('Could not load data for airfoil '+ a_name)
        continue


    # Ensure bad airfoils are dealt with - send them to bad folder
    try:
        af = Airfoil(a_name,Ma,Re)
        px = af.pixel_grid()
    except:
        shutil.move('{}\\{}.dat'.format(in_dir,a_name),'aero_shape_opt\\datasets\\bad_airfoils')
        continue

    #coords = coords.flatten() # flatten to a vector of [x1,y1,x2,y2,...]
    # Extract each [AoA, CL, CD, CDp, CM, Top_xtr, Bot_xtr]
    if len(xdata) > 12:
        polar_nums = np.array([re.findall(r'[-+]?\d+[\.\,\d]*\d*',line) for line in xdata[12:]], dtype='float32')
    else:
        print('Could not load data for airfoil '+ a_name)
        continue

    # The input vector to the ANN
    # input = 
    if len(polar_nums) < 1:
        continue

    # Create an input for each angle of attack
    for polar_line in polar_nums:
        aoa = polar_line[0]
        CL = polar_line[1]
        CD = polar_line[2]
        CM = polar_line[4]

        # [x1,y1,x2,y2,...,Re,Ma,AoA]
        input = [px,Re,Ma,aoa]
        #input = np.append(px,(Re,Ma,aoa))
        output = [CL,CD,CM]

        # airfoil_inputs.append(input.tolist())
        airfoil_inputs.append(input)
        airfoil_outputs.append(output)


# Ratio of test data 
test = 0.2
# SHOULD WE SPLIT DATA HERE, OR WHEN WE IMPORT IT FOR ANN???

# Each element of the input data consists of: [x1,y1,x2,y2,...,Re,Ma,AoA]
# Each element of the output data consists of: [CL,CD,CM]]
print(len(airfoil_outputs))
print('Almost done')
np.savez('aero_shape_opt\\datasets\\data_file',input=airfoil_inputs,output=airfoil_outputs)
print('Done')

# TO IMPORT THE NEWLY CREATED FILE:
data = np.load('aero_shape_opt\\datasets\\data_file.npz',allow_pickle=True)
inp = data['input']
out = data['output']






