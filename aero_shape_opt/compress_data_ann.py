# Compress airfoil data into a single .npz folder for easier extraction later

import os
import math
import numpy as np
import re
import warnings
import random

airfoil_names = []
in_dir = "aero_shape_opt\\datasets\\airfoil_gen"
out_dir = "aero_shape_opt\\datasets\\xfoil_data_spline"

# Get list of airfoil names
# for filename in os.listdir(in_dir):
#     if filename.endswith(".dat"):
#         name = filename[0:filename.find('.')]
#         airfoil_names.append(name)
for filename in os.listdir(in_dir):
    if "_CP" in filename:
        name = filename[0:filename.find('_')]
        airfoil_names.append(name)

airfoil_inputs = []
airfoil_outputs = []
num_afiles = 0
err_num = 0
# Get airfoil information
for a_name in airfoil_names:
    #coord_name = a_name + "_airfoil.txt"
    coord_name = a_name + "_CP.dat"
    polar_name = a_name + "_polar.txt"
    
    try:
        # Coordinates. Turn off empty file warnings, since is caught
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            #coords = np.loadtxt(out_dir + "\\" + coord_name)
            coords = np.loadtxt(in_dir + "\\" + coord_name,skiprows=1)
        coords = coords.flatten() # flatten to a vector of [x1,y1,x2,y2,...]

        # if(len(coords) > 340):
        #     print('Too many coordinate points for airfoil '+ a_name)
        #     continue

        # Extract all polar data
        f = open(out_dir + "\\" + polar_name, 'r')
        xdata = f.read()
        f.close()
    except:
        print('Could not load data for airfoil '+ a_name)
        continue

    xdata = xdata.splitlines()

    # Extract [Mach no., Reynold n., Ncrit]
    header_nums = re.findall(r'[-+]?\d+\.*\d*[ e ]*\d*', xdata[8])
    header_nums = [float(a.replace(" ","")) for a in header_nums]    
    Ma = header_nums[0]
    Re = header_nums[1]

    # Extract each [AoA, CL, CD, CDp, CM, Top_xtr, Bot_xtr]
    if len(xdata) > 12:
        num_afiles = num_afiles + 1
        polar_nums = np.array([re.findall(r'[-+]?\d+[\.\,\d]*\d*',line) for line in xdata[12:]], dtype='float32')
    else:
        print('Could not load data for airfoil '+ a_name)
        err_num = err_num+1
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
        #input = np.append(coords,(Re,Ma,aoa))
        # for i,c in zip(range(len(coords)),coords):
	    #     if i % 2 != 0:
		#         coords[i] = (coords[i]+0.1)/0.5
        #input = np.append(coords,(aoa+2)/8)
        input = np.append(coords,aoa)
        #output = [CL,CD,CM]
        #output = [(CL+.5)/2.5]
        output = CL

        airfoil_inputs.append(input.tolist())
        airfoil_outputs.append(output)


# Ratio of train data 
train = 0.8

# Each element of the input data consists of: [x1,y1,x2,y2,...,Re,Ma,AoA]
# Each element of the output data consists of: [CL,CD,CM]]
print(len(airfoil_outputs))
print('Almost done')
order = [i for i in range(len(airfoil_inputs))]
random.shuffle(order)
inp_train = [airfoil_inputs[i] for i in order[:math.ceil(train*len(airfoil_inputs))]]
inp_test =  [airfoil_inputs[i] for i in order[math.ceil(train*len(airfoil_inputs)):]]
out_train = [airfoil_outputs[i] for i in order[:math.ceil(train*len(airfoil_outputs))]]
out_test =  [airfoil_outputs[i] for i in order[math.ceil(train*len(airfoil_outputs)):]]

np.savez('aero_shape_opt\\datasets\\data_file_ann',x_train=inp_train,x_test=inp_test,y_train=out_train,y_test=out_test)

# TO IMPORT THE NEWLY CREATED FILE:
data = np.load('aero_shape_opt\\datasets\\data_file_ann.npz',allow_pickle=True)
x_train = data['x_train']
x_test = data['x_test']
y_train = data['y_train']
y_test = data['y_test']

print('Done')
print(num_afiles)
print(err_num)

