import numpy as np
import matplotlib.pyplot as plt
import numpy as np

from astropy.io.fits.hdu import image
from astropy.io import fits

hdul=fits.open("/home/oem/Imágenes/Fermi_CCDsImages_2021/images/test_ruido_v2/skp2rooted/proc/proc_init_lta_ICN_E120_NSAMP_16_img_17.fits")

active_mask = np.s_[:, 9:538]

data= hdul[0].data

stdDev = np.std(data[active_mask])		# Standard deviation
meanVal= np.mean(data[active_mask])

mu, sigma = meanVal, stdDev/meanVal

count, bins, ignored = plt.hist(data[active_mask], 30, density=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()
