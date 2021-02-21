from airfoil import Airfoil

name = 'mh32'
M = 0 # Mach number
Re = 500000 # Reynolds number
af = Airfoil(name,M,Re)

path = 'mh32.dat'
af.setXCoordsFromPath()
af.setYCoordsFromPath()
pixels = af.pixel_grid()
print(pixels)
print(len(pixels))
print(len(pixels[0]))