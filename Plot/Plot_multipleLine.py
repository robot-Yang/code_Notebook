# -*- coding: utf-8 -*-
# @Author: Yang Chen
# @Date:   2020-06-09 23:28:51
# @Last Modified by:   chenyang
# @Last Modified time: 2020-06-10 03:40:41

# test example for plotting multiple line in one single fig by 2D matrix
 
import matplotlib.pyplot as plt
import numpy as np
from random import random

x = np.random.random((5,5))
y = np.random.random((5,5))
print(x[:,1])

drawLines = []
for i in range(len(x)):
	drawLines.append(x[i])
	drawLines.append(y[i])

plt.plot(drawLines,label = 'first 2 lines')
plt.legend()
plt.show()

