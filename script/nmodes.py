#
# compute number of independent modes in k bins
#
# Output:
#     Column 1: k (centre of bin)
#     Column 2: number of independent modes

import math
import argparse
import numpy as np
import math


parser = argparse.ArgumentParser()
parser.add_argument('--nc', type=int, default='64',
                    help='number of grids in each dimension')
parser.add_argument('--boxsize', type=float, default=1000.0,
                    help='length of a cubic box on a side [1/h Mpc]')
parser.add_argument('--k-unit', type=int, default=1,
                    help='0: fundamental frequency, 1: h/Mpc')
parser.add_argument('--k-min', type=float, default=0.0)
parser.add_argument('--k-max', type=float, default=1.0)
parser.add_argument('--dk', type=float, default=0.01, help='bin width')

arg = parser.parse_args()

nc = arg.nc

if arg.k_unit == 0:
    fac = 1.0
else:
    fac = 2.0*math.pi/arg.boxsize
    
kmin = arg.k_min
kmax = arg.k_max
dk =   arg.dk

nbin = round((kmax - kmin)/dk)

nmodes  = np.zeros(nbin)

for ix in range(-nc//2, nc//2):
    for iy in range(-nc//2, nc//2):
        for iz in range(-nc//2, nc//2):
            k = fac*math.sqrt(ix**2 + iy**2 + iz**2)
            index = int(math.floor((k - kmin)/dk))
            if 0 <= index and index < nbin:
                nmodes[index] +=  1.0
            
for i in range(nbin):
    if kmin + (i + 0.5)*dk < nc / 2:
        print("%e %.1f" % (
            kmin + (i + 0.5)*dk,
            nmodes[i]/2))
