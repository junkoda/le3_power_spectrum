import argparse
import struct
import numpy as np

def read(filename):
    """Read binary grid data and return as numpy array"""
    with open(filename, 'rb') as f:
        nc = struct.unpack('i', f.read(4))[0]
        a = np.zeros((nc, nc, nc))
        for ix in range(nc):
            for iy in range(nc):
                for iz in range(nc):
                    a[ix, iy, iz] = struct.unpack('f', f.read(4))[0]
        nc_check = struct.unpack('i', f.read(4))[0]
        assert(nc == nc_check)

        return a

# def plot():
#     import matplotlib.pyplot as plt
#     import matplotlib.cm as cm

#     grid = read_grid('grid_begenning.b')
#     plt.imshow(grid1[:,:, 32], cmap=cm.gist_rainbow)
#     #plt.savefig('grid.pdf')
