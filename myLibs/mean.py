#basic libraries
import os
import glob
import sys
from astropy.io.fits.hdu import image
import numpy as np
from astropy.stats import median_absolute_deviation as mad
from astropy.io import fits
from matplotlib import pyplot as plt
from math import sqrt

import pandas as pd

def mean(fileList,optionList):
    #list of files
    #list of commands

    fileList.sort(key=os.path.getmtime)           #####  lista los archivos en los argumentos del cmd

    # Define active and overscan areas
    active_mask = np.s_[:, 9:538]		#   9 <= x < 538
    overscan_mask = np.s_[:, 538:]		# 538 <= x
    mask=overscan_mask	# Area where variable will be computed

    for image in fileList:
        try:
            hdul=fits.open(image)
        except:
            break
        
        plt.hist(hdul, bins=256, range=(0.0, 1.0), fc='k', ec='k')

    plt.show()

    return