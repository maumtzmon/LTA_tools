#!/usr/bin/python3
import os
import glob
import sys
import numpy as np
from astropy.stats import median_absolute_deviation as mad
from astropy.io import fits
from matplotlib import pyplot as plt

import pandas as pd



if len(sys.argv) > 1:
	files = sys.argv[1:]
	files.sort(key=os.path.getmtime)

#	latest_file = max(files, key=os.path.getctime)
#	print(latest_file)
#	image='image.fz'

	# Define active and overscan areas
	active_mask = np.s_[:, 9:538]		#   9 <= x < 538
	overscan_mask = np.s_[:, 538:]		# 538 <= x

	mask=overscan_mask	# Area where variable will be computed

	array=[]

#	datafile=open(r"meanvsvdrain.txt","a+")
#	datafile.write("#VDRAIN\tMean_ext1\tMean_ext2\tMean_ext3\tMean_ext4\n")

	for image in files:

#		print(image)
		hdul=fits.open(image)
#		hdul.info()

		stdDev=[]
		meanVal=[]
		medVal=[]

		

#		for i in range(0,1):
		for i in range(0, len(hdul)):

			# Load data and header
			data=hdul[i].data
			header=hdul[i].header

			if data is not None:				# Check if data is not empty

#				data = data - np.median(data, axis=0, keepdims=True)			# Subtract median per column
#				data = data - np.median(data[overscan_mask], axis=1, keepdims=True)	# Subtract OS median per row

				stdDev.append(np.std(data[mask]))		# Standard deviation
				meanVal.append(np.mean(data[mask]))		# Mean
				medVal.append(np.median(data[mask]))	# Median

				# Extract info from header
#				string=header['NSAMP']
#				string=header['PSAMP']
#				string=header['DGAH']
#				string=header['VDRAIN']

				string=header['RUNID']

		# Extract info from img title
#		string=image.split("img")[1].split(".")[0]		# To obtain imgID
#		string=image.split("PSAMP")[1].split("_")[0]		# To obtain PSAMP
#		string=image.split("NSAMP")[1].split("_")[0]		# To obtain NSAMP

		#varNp=np.array(var)
		
		print(string, stdDev[0], stdDev[1], stdDev[2], stdDev[3])#, var[4], var[5], var[6], var[7], "\n")
	
# 		array.append([string, var[0], var[1], var[2], var[3]])

	
#	plt.plot(var[12000:])
#	plt.show()

#	np.savetxt(datafile, array, fmt="%s")	# Save array to datafile
#	datafile.close()			# Close datafile

else:
	print("To run do: python3 checknoise.py path/img*.fits")
