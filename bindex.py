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
# Output: Numerical representation of the convexity (BI).
# =============================================================================
def beer_index(image):
    #structuringElement=np.ones((3,3))):
    
    theImage=np.pad(image,1,constant_values=0)
    # Use "selem" instead of "footprint" or vice-versa depending on skimage version
    # Generating padding around the binary image array with value=0.
    
    theObject=np.argwhere(theImage)
    # Obtains the indices of the elements in the image array which are 1s.
    
    numPixObject=theObject.shape[0]
    # Returns the number of 1s in the image array. 
    
    visMatrix=np.zeros((numPixObject,numPixObject))
    # Generating a matrix of 0s. Size: numPixObject x numPixObject. After the complete
    # procedure, each position will indicate the visibility between two pixels, witg 1 
    # representing visible points and 0 representing non-visible ones. 
    
    for iFirst in range(numPixObject-1):
        rStart,cStart=theObject[iFirst]
        for iSecond in range(iFirst+1,numPixObject):
            rLine,cLine=line(rStart,cStart,*theObject[iSecond])
            theValue=theImage[rLine,cLine].all()
            visMatrix[iFirst,iSecond]=theValue
            visMatrix[iSecond,iFirst]=theValue
    return np.mean(visMatrix.sum(axis=1)/(numPixObject-1))
    # Two loops iterate over all pair of pixels. 
    # For every pair of pixels, the Line function gives the indices of the pixels 
    # in between.
    # These interimediate pixels are verified: one the one hand, if all of their values 
    # are 1s, then we consider that this pair of pixels are visible and the visMatrix is 
    # updated with "True" in the corresponding position. On the other hand, if any of them 
    # is 0, then we consider that the pair of pixels is not visible and the visMatrix is 
    # updated with "False". 
    # Once the visMatrix is completed, for each pixel, we determine how many other pixels 
    # it can see or, in other words, its visibility. 
    # Finally, the BI is obtained as the mean of the visibility values of all individual
    # pixels divided by area of the object.  











