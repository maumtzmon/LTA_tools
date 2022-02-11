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


def noise(fileList,optionList):
    #list of files
    #list of commands

    fileList.sort(key=os.path.getmtime)           #####  lista los archivos en los argumentos del cmd
    
    # Define active and overscan areas
    active_mask = np.s_[:, 9:538]		#   9 <= x < 538
    overscan_mask = np.s_[:, 538:]		# 538 <= x
    mask=overscan_mask	# Area where variable will be computed

    statistics={}
    
    statistics['header'] ={'runID':[],'sqrt_NSAMP':[]}
    statistics['stdDev'] ={'runID':[],'sqrt_NSAMP':[],'ohdu_1':[],'ohdu_2':[],'ohdu_3':[],'ohdu_4':[]}
    statistics['meanVal']={'runID':[],'sqrt_NSAMP':[],'ohdu_1':[],'ohdu_2':[],'ohdu_3':[],'ohdu_4':[]} 
    statistics['medVal'] ={'runID':[],'sqrt_NSAMP':[],'ohdu_1':[],'ohdu_2':[],'ohdu_3':[],'ohdu_4':[]}

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
                sqrt_NSAMP=str(sqrt(int(header['NSAMP'])))

        statistics['header']['runID'].append(string)
        statistics['header']['sqrt_NSAMP'].append(sqrt_NSAMP)
        statistics['stdDev']['runID'].append(string)
        statistics['stdDev']['sqrt_NSAMP'].append(sqrt_NSAMP)
        statistics['meanVal']['runID'].append(string)
        statistics['meanVal']['sqrt_NSAMP'].append(sqrt_NSAMP)
        statistics['medVal']['runID'].append(string)
        statistics['medVal']['sqrt_NSAMP'].append(sqrt_NSAMP)

        if 'S' in optionList:
            statistics['stdDev']['ohdu_1'].append(stdDev[0])          # stdDev[0], stdDev[1], stdDev[2], stdDev[3]
            statistics['stdDev']['ohdu_2'].append(stdDev[1])
            statistics['stdDev']['ohdu_3'].append(stdDev[2])
            statistics['stdDev']['ohdu_4'].append(stdDev[3])
        
        if 'M' in optionList:
            statistics['meanVal']['ohdu_1'].append(meanVal[0])        # meanVal[0], meanVal[1], meanVal[2], meanVal[3]
            statistics['meanVal']['ohdu_2'].append(meanVal[1])
            statistics['meanVal']['ohdu_3'].append(meanVal[2])
            statistics['meanVal']['ohdu_4'].append(meanVal[3])
        
        if 'm' in optionList:
            statistics['medVal']['ohdu_1'].append(medVal[0])          # medVal[0], medVal[1], medVal[2], medVal[3]
            statistics['medVal']['ohdu_2'].append(medVal[1])
            statistics['medVal']['ohdu_3'].append(medVal[2])
            statistics['medVal']['ohdu_4'].append(medVal[3])   



    if 'S' in optionList:
        stdDev_df=pd.DataFrame.from_dict(statistics['stdDev'])
        print('Check Noise\n\nStandar Deviation\n')
        print(stdDev_df.round(3))
    if 'M' in optionList:
        Mean_df=pd.DataFrame.from_dict(statistics['meanVal'])
        print('\nMean\n')
        print(Mean_df.round(3))
    if 'm' in optionList:
        median_df=pd.DataFrame.from_dict(statistics['medVal'])
        print('\nMedian\n')
        print(median_df.round(3))
        
    #plot each column for StdDev

    #stdDev_df.plot()
    # stdDev_df.plot(x='sqrt_NSAMP', y='ohdu_1')   ### Plot despliega solo los elementos del dataframe que necesitas indicando el eje coordenado
    # stdDev_df.plot(x='sqrt_NSAMP', y='ohdu_2')
    # stdDev_df.plot(x='sqrt_NSAMP', y='ohdu_3')
    # stdDev_df.plot(x='sqrt_NSAMP', y='ohdu_4')

    

    #fig=plt.figure(figsize=[8,8])
    fig, axes=plt.subplots(2, 2, figsize=[9.5,8.5])
    fig.suptitle('Std Dev vs ADUs/sqrt(NSAMP)')
    
    axes[0,0].plot(statistics['stdDev']['sqrt_NSAMP'],statistics['stdDev']['ohdu_1'])
    axes[0,1].plot(statistics['stdDev']['sqrt_NSAMP'],statistics['stdDev']['ohdu_2'])
    axes[1,0].plot(statistics['stdDev']['sqrt_NSAMP'],statistics['stdDev']['ohdu_3'])
    axes[1,1].plot(statistics['stdDev']['sqrt_NSAMP'],statistics['stdDev']['ohdu_4'])
    axes[0, 0].set_title('ohdu_1')
    axes[0, 1].set_title('ohdu_2')
    axes[1, 0].set_title('ohdu_3')
    axes[1, 1].set_title('ohdu_4')
    
    # for ax in axes.flat:
    #     ax.set(xlabel='sqrt(NSAMP)', ylabel='ADUs')

    axes[0, 0].set(ylabel='ADUs')
    axes[1, 0].set(xlabel='sqrt(NSAMP)', ylabel='ADUs')
    axes[1, 1].set(xlabel='sqrt(NSAMP)')
    
    if 'p' in optionList:
        plt.show()
    


    return 0