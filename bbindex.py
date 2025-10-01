#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# BEER BOUNDARY INDEX (BBI)
#
# Description : Computes the BBI to evaluate shape convexity.
# Author      : Miquel Àngel Serra (Science & Code)
#               Arnau Mir (Science & Code)
#               Antoni Burguera (Science % Code)
#               Oscar Valero (Science & Code)
###############################################################################

###############################################################################
# IMPORTS
###############################################################################

import numpy as np
from skimage.draw import line
from skimage.morphology import binary_erosion

###############################################################################
# MAIN FUNCTION
###############################################################################

# =============================================================================
# BEER_BOUNDARY_INDEX
#
# Compute the Beer Boundary Index
#
# Input  : theImage           - binary image array.
#          structuringElement - contour neighborhood. Default is 8-neighbours.
#                               None is 4-neighbours.
# =============================================================================
def beer_boundary_index(theImage,structuringElement=np.ones((3,3))):
    theImage=np.pad(theImage,1,constant_values=0)
    # Use "selem" instead of "footprint" or vice-versa depending on skimage version
    theContour=np.argwhere(theImage-binary_erosion(theImage,footprint=structuringElement))
    numPixContour=theContour.shape[0]
    visMatrix=np.zeros((numPixContour,numPixContour))
    for iFirst in range(numPixContour-1):
        rStart,cStart=theContour[iFirst]
        for iSecond in range(iFirst+1,numPixContour):
            rLine,cLine=line(rStart,cStart,*theContour[iSecond])
            theValue=theImage[rLine,cLine].all()
            visMatrix[iFirst,iSecond]=theValue
            visMatrix[iSecond,iFirst]=theValue
    return np.mean(visMatrix.sum(axis=1)/(numPixContour-1))
