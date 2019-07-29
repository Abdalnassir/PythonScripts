'''
Data visualzation with matplotlib
'''

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# create array for x and y
x = np.arange(0,10)

y = x**2

# plot the values 

plt.plot(x,y)


# optional - add limits
plt.xlim(0,4)
plt.ylim(0,4)

# optional - add title
plt.title("Some Title")

# optional - add labels for x and y axis
plt.xlabel("X")
plt.ylabel("Y")

# finally show the chart
plt.show()