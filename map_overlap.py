# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:35:32 2019

@author: Gareth Lomax
"""

"""
functions to test finding location of prio grid cutout
"""

# prio grid is 360 * 720, and of dimension i,  j

import numpy as np
import matplotlib.pyplot as plt


#
#test = np.zeros((5,5))
#test[1,0] = 20
#print(test)
def captured_test(im_i, im_j, event_i, event_j, dim = 16):
    """simple test to check out of arrays of i and j locations of upper left pixel
    of images of edge size dim (square) if the event is located inside.

    im_i, im_j are numpy arrays

    uses nice numpy bool logic
    - find bool arrays, multiply together to find union of two sets of correct
    coords.
    """

    dist_i = event_i - im_i # find relative distances in i and j directions
    dist_j = event_j - im_j

    #TODO: DOUBLE CHECK THESE BOUNDS

    # positive bounds
    b_i = dist_i < dim # i.e must be at most 16 blocks away?
    b_j = dist_j < dim

    # negative bounds

    bn_i = -1 < dist_i
    bn_j = -1 < dist_j

    # now multiply to find where images are
    containing_coords_bool = b_i * b_j * bn_i * bn_j

    return containing_coords_bool

#im_i = np.array([0,213,23,4])
#im_j = np.array([0,2,4,15])
#
#print(captured_test(im_i, im_j, 4,15))
def construct_overlap_map(i_loc, j_loc,pred_maps, dim = 16, filename = False):
    """function to overlay array onto map. Constructs map of incidence.
    """
    p_map = np.zeros((360,720)) # sets up basis maps
    n_map = np.zeros_like(p_map)

    ones_array = np.ones((dim,dim))

    # this doesnt really need to be efficient
    for ind, (i, j) in enumerate(zip(i_loc, j_loc)):
        n_map[i: i + dim, j: j + dim] += ones_array
        p_map[i: i + dim, j: j + dim] += pred_maps[ind]

    if filename is not False:
        np.save("{}_n_map".format(filename),n_map)
        np.save("{}_p_map".format(filename),p_map)

    return n_map, p_map





#    n_map =
#    plt.figure()
#    plt.imshow(n_map)
#    plt.figure()
#    plt.imshow(p_map)

#
#a = np.random.randint(low = 0, high = 360 - 16, size = 200000)
#b = np.random.randint(low = 0, high = 720 - 16, size = 200000)
#pred_maps = np.random.uniform(size = (200000, 16,16))
#
#construct_overlap_map(a, b, pred_maps)
#
#




