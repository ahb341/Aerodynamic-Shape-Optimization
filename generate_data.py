import os
import numpy as np
import matplotlib.pyplot as plt

curDir = os.getcwd()
AoA        = '0'
numNodes   = '170'
saveFlnmAF = 'Save_Airfoil.txt'
saveFlnmCp = 'Save_Cp.txt'
xfoilFlnm  = 'xfoil_input.txt'

# Delete files if they exist
if os.path.exists(saveFlnmAF):
    os.remove(saveFlnmAF)
if os.path.exists(saveFlnmCp):
    os.remove(saveFlnmCp)

dir = os.getcwd() + '\\datasets\\airfoils'
for filename in os.listdir(dir):
    if filename.endswith(".dat"):
        print(os.path.join(dir, filename))
        print('\\datasets\\airfoils' + filename)
    else:
        continue

    # Create the airfoil
# fid = open(xfoilFlnm,"w")
# #fid.write("NACA " + NACA + "\n")
# fid.write("load airfoils/" + )
# fid.write("PPAR\n")
# fid.write("N " + numNodes + "\n")
# fid.write("\n\n")
# fid.write("PSAV " + saveFlnmAF + "\n")
# fid.write("OPER\n")
# fid.write("ALFA " + AoA + "\n")
# fid.write("CPWR " + saveFlnmCp + "\n")
# fid.close()