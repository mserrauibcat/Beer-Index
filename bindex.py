#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# BEER INDEX (BI)
#
# Description : Computes the BI to evaluate shape convexity.
# Author      : Miquel Àngel Serra (Science & Code)
#               Arnau Mir (Science & Code)
#               Antoni Burguera (Code)
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
# BEER_INDEX
#
# Compute the Beer Index
#
# Input  : theImage           - binary image array.
#          structuringElement - contour neighborhood. Default is 8-neighbours.
#                               None is 4-neighbours.
# =============================================================================
def beer_index(image):
    #structuringElement=np.ones((3,3))):
    theImage=np.pad(image,1,constant_values=0)
    # Use "selem" instead of "footprint" or vice-versa depending on skimage version
    
    theObject=np.argwhere(theImage)
    
    numPixObject=theObject.shape[0]

    
    visMatrix=np.zeros((numPixObject,numPixObject))
    
    for iFirst in range(numPixObject-1):
        rStart,cStart=theObject[iFirst]
        for iSecond in range(iFirst+1,numPixObject):
            rLine,cLine=line(rStart,cStart,*theObject[iSecond])
            theValue=theImage[rLine,cLine].all()
            visMatrix[iFirst,iSecond]=theValue
            visMatrix[iSecond,iFirst]=theValue
    return np.mean(visMatrix.sum(axis=1)/(numPixObject-1))