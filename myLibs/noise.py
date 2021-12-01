#basic libraries
import os
import glob
import sys
from astropy.io.fits.hdu import image
import numpy as np
from astropy.stats import median_absolute_deviation as mad
from astropy.io import fits
from matplotlib import pyplot as plt

import pandas as pd


def noise(fileList,optionList):
    #list of files
    #list of commands

    fileList.sort(key=os.path.getmtime)
    
    # Define active and overscan areas
    active_mask = np.s_[:, 9:538]		#   9 <= x < 538
    overscan_mask = np.s_[:, 538:]		# 538 <= x
    mask=overscan_mask	# Area where variable will be computed

    statistics={}
    
    statistics['header'] ={'runID':[]}
    statistics['stdDev'] ={'runID':[],'ohdu_1':[],'ohdu_2':[],'ohdu_3':[],'ohdu_4':[]}
    statistics['meanVal']={'runID':[],'ohdu_1':[],'ohdu_2':[],'ohdu_3':[],'ohdu_4':[]} 
    statistics['medVal'] ={'runID':[],'ohdu_1':[],'ohdu_2':[],'ohdu_3':[],'ohdu_4':[]}

    array=[]

    for image in fileList:
        try:
            hdul=fits.open(image)
        except:
            break
        stdDev=[]
        meanVal=[]
        medVal=[]
        
        for i in range(0, len(hdul)):
            data=hdul[i].data
            header=hdul[i].header   
            if data is not None:				# Check if data is not empty
                if 'S' in optionList:
                    stdDev.append(np.std(data[mask]))		# Standard deviation
                if 'M' in optionList:
                    meanVal.append(np.mean(data[mask]))		# Mean
                if 'm' in optionList:
                    medVal.append(np.median(data[mask]))    # median
    
                
                string=header['RUNID']

        statistics['header']['runID'].append(string)
        statistics['stdDev']['runID'].append(string)
        statistics['meanVal']['runID'].append(string)
        statistics['medVal']['runID'].append(string)

        if 'S' in optionList:
            statistics['stdDev']['ohdu_1'].append(stdDev[0])          # stdDev[0], stdDev[1], stdDev[2], stdDev[3]
            statistics['stdDev']['ohdu_2'].append(stdDev[1])
            statistics['stdDev']['ohdu_3'].append(stdDev[2])
            statistics['stdDev']['ohdu_4'].append(stdDev[3])
        
        if 'M' in optionList:
            statistics['meanVal']['ohdu_1'].append(meanVal[0])          # meanVal[0], meanVal[1], meanVal[2], meanVal[3]
            statistics['meanVal']['ohdu_2'].append(meanVal[1])
            statistics['meanVal']['ohdu_3'].append(meanVal[2])
            statistics['meanVal']['ohdu_4'].append(meanVal[3])
        
        if 'm' in optionList:
            statistics['medVal']['ohdu_1'].append(medVal[0])          # medVal[0], medVal[1], medVal[2], medVal[3]
            statistics['medVal']['ohdu_2'].append(medVal[1])
            statistics['medVal']['ohdu_3'].append(medVal[2])
            statistics['medVal']['ohdu_4'].append(medVal[3])   



    if 'S' in optionList:
        df=pd.DataFrame.from_dict(statistics['stdDev'])
        print(df)
    if 'M' in optionList:
        df=pd.DataFrame.from_dict(statistics['meanVal'])
        print(df)
    if 'm' in optionList:
        df=pd.DataFrame.from_dict(statistics['medVal'])
        print(df)
        # print(string, stdDev[0], stdDev[1], stdDev[2], stdDev[3])#, var[4], var[5], var[6], var[7], "\n")
        # data2print=str(string)+';'+str(stdDev[0])+';'+str(stdDev[1])+';'+str(stdDev[2])+';'+str(stdDev[3])+'\n'
        # f=open('proc_stdDev.csv','a')
        # f.write(data2print)
        # f.close()
    


    return 0