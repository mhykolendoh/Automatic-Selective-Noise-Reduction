import numpy as np
from scipy import misc
image  = misc.imread('test.png',mode="L")
noislv1 = image + 1 * image.std() * np.random.random(image.shape)
hnoise  = 2 * image.max() * np.random.random(image.shape)
noislv2 = image + hnoise

import matplotlib.pyplot as plt
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(image,cmap = plt.get_cmap('gray'))
axarr[0, 0].set_title('Original')

axarr[0, 1].imshow(noislv1,cmap = plt.get_cmap('gray'))
axarr[0, 1].set_title('Noise Lv.1')

axarr[1, 0].imshow(noislv2,cmap = plt.get_cmap('gray'))
axarr[1, 0].set_title('Noise Lv.2')

axarr[1, 1].imshow(hnoise,cmap = plt.get_cmap('gray'))
axarr[1, 1].set_title('Noise')


plt.show()
