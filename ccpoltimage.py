'''
Create and visualize image with matplotlib
'''

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# create a matrix
mat = np.arange(0,100).reshape(10,10)

# generate image
plt.imshow(mat)

#optional
plt.colorbar()
# show image
plt.show()