#!/usr/bin/env python

## https://joshuagoings.wordpress.com/2013/05/14/efficient-two-electron-integral-transformations-in-python-or-adventures-in-scaling/

from __future__ import print_function
from __future__ import division

import numpy as np


def ao2mo_original_n8(INT, C):

    dim = INT.shape[0]
    MO = np.zeros(shape=(dim, dim, dim, dim))

    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for l in range(dim):
                    for m in range(dim):
                        for n in range(dim):
                            for o in range(dim):
                                for p in range(dim):
                                    MO[i,j,k,l] += C[i,m]*C[j,n]*C[k,o]*C[l,p]*INT[m,n,o,p]

    return MO


def ao2mo_original_n5(INT, C):

    dim = INT.shape[0]
    MO = np.zeros(shape=(dim, dim, dim, dim))

    temp1 = np.zeros((dim, dim, dim, dim))
    temp2 = np.zeros((dim, dim, dim, dim))
    temp3 = np.zeros((dim, dim, dim, dim))

    for i in range(dim):
        for m in range(dim):
            temp1[i,:,:,:] += C[i,m]*INT[m,:,:,:]
        for j in range(dim):
            for n in range(dim):
                temp2[i,j,:,:] += C[j,n]*temp1[i,n,:,:]
            for k in range(dim):
                for o in range(dim):
                    temp3[i,j,k,:] += C[k,o]*temp2[i,j,o,:]
                for l in range(dim):
                    for p in range(dim):
                        MO[i,j,k,l] += C[l,p]*temp3[i,j,k,p]

    return MO
