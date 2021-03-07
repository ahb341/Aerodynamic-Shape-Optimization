import os
import numpy as np
import matplotlib.pyplot as plt
import subprocess

def main():
    alphas        = ['-2','6']
    numNodes   = '170'
    Re = '500000'             # Reynolds number
    M = '0'                   # Mach number (incompressible flow)

    dir = os.getcwd() + '\\aero_shape_opt\\datasets\\airfoils'
    n = 0
    for filename in os.listdir(dir):
        if filename.endswith(".dat"):
            # print(os.path.join(dir, filename))
            # print('\\datasets\\airfoils\\' + filename)
            name = filename[0:filename.find('.')]
            runXfoil(name,filename,numNodes,alphas,Re,M)
            n = n+1
            print(n)
        else:
            continue

def runXfoil(name,filename,numNodes,alphas,Re,M):
    saveFlnmAF = name + '_airfoil.txt'
    saveFlnmPolar = name + '_polar.txt'
    xfoilFlnm  = 'xfoil_input.txt'
    inc = '0.25' # increment for angle of attack sequence

    # Delete files if they exist
    if os.path.exists('aero_shape_opt\\datasets\\xfoil_data\\' + saveFlnmAF):
        os.remove('aero_shape_opt\\datasets\\xfoil_data\\' + saveFlnmAF)
    if os.path.exists(os.getcwd() + '\\aero_shape_opt\\datasets\\xfoil_data\\' + saveFlnmPolar):
        os.remove('aero_shape_opt\\datasets\\xfoil_data\\' + saveFlnmPolar)

    # Create the airfoil
    fid = open(xfoilFlnm,"w")
    fid.write("PLOP\ng\n\n")
    fid.write("load aero_shape_opt/datasets/airfoils/" + filename + "\n")
    fid.write("PPAR\n")
    fid.write("N " + numNodes + "\n")
    fid.write("\n\n")
    fid.write("PSAV aero_shape_opt/datasets/xfoil_data/" + saveFlnmAF + "\n")
    fid.write("OPER\n")
    fid.write("VISC " + Re + " \n")
    fid.write("MACH " + M + " \n")
    fid.write("ITER 200\n")
    fid.write("PACC\n")
    fid.write("aero_shape_opt/datasets/xfoil_data/" + saveFlnmPolar + "\n")
    fid.write("\n")
    fid.write("ASEQ " + alphas[0] + " " + alphas[1] + " " + inc + "\n")
    fid.write("PACC\n")
    fid.write("\n")
    fid.write("QUIT\n")
    fid.close()
    # Run the XFoil calling command
    # os.system("{}\\aero_shape_opt\\datasets\\xfoil.exe < {}".format(os.getcwd(),xfoilFlnm))
    f = open(xfoilFlnm,'r')
    p = subprocess.Popen("{}\\aero_shape_opt\\datasets\\xfoil.exe".format(os.getcwd()),stdin=f)
    # xfoilFlnm))
    try:
        # p.wait(15)
        p.communicate(timeout=30)
    except subprocess.TimeoutExpired:
        p.kill()
        p.communicate()
        
    f.close()
    # Delete file after running
    if os.path.exists(xfoilFlnm):
        os.remove(xfoilFlnm)
    
def readData(saveFlnmAF):
    # %% READ DATA FILE: AIRFOIL
    # Load the data from the text file
    dataBuffer = np.loadtxt(saveFlnmAF, skiprows=0)
    # Extract data from the loaded dataBuffer array
    XB = dataBuffer[:,0]
    YB = dataBuffer[:,1]
    # Delete file after loading
    if os.path.exists(saveFlnmAF):
        os.remove(saveFlnmAF)
    # %% READ DATA FILE: PRESSURE COEFFICIENT
    # Load the data from the text file
    dataBuffer = np.loadtxt(saveFlnmCp, skiprows=3)
    # Extract data from the loaded dataBuffer array
    X_0  = dataBuffer[:,0]
    Y_0  = dataBuffer[:,1]
    Cp_0 = dataBuffer[:,2]
    # Delete file after loading
    if os.path.exists(saveFlnmCp):
        os.remove(saveFlnmCp)
    # %% EXTRACT UPPER AND LOWER AIRFOIL DATA
    # Split airfoil into (U)pper and (L)ower
    XB_U = XB[YB >= 0]
    XB_L = XB[YB < 0]
    YB_U = YB[YB >= 0]
    YB_L = YB[YB < 0]
    # Split XFoil results into (U)pper and (L)ower
    Cp_U = Cp_0[YB >= 0]
    Cp_L = Cp_0[YB < 0]
    X_U  = X_0[YB >= 0]
    X_L  = X_0[YB < 0]
    # %% PLOT DATA
    # Plot airfoil
    fig = plt.figure(1)
    plt.cla()
    plt.plot(XB_U,YB_U,'b.-',label='Upper')
    plt.plot(XB_L,YB_L,'r.-',label='Lower')
    plt.xlabel('X-Coordinate')
    plt.ylabel('Y-Coordinate')
    plt.title('Airfoil')
    plt.axis('equal')
    plt.legend()
    plt.show()
    # Plot pressure coefficient
    fig = plt.figure(2)
    plt.cla()
    plt.plot(X_U,Cp_U,'b.-',label='Upper')
    plt.plot(X_L,Cp_L,'r.-',label='Lower')
    plt.xlim(0,1)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Pressure Coefficient')
    plt.show()
    plt.legend()
    plt.gca().invert_yaxis()

main()