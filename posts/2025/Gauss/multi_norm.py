import os
import numpy as np
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__), "height_weight.txt")
os.chdir()

data = np.loadtxt("height_weight.txt")
print(data.shape)
height = data[:, 0]
weight = data[:, 1]

small_data = data[0:500]
plt.scatter(small_data[:, 0], small_data[:, 1])
plt.xlabel("height(cm)")
plt.ylabel("weight(kg)")
plt.show()

mu = np.mean(data, axis=0)
cov = np.cov(data, rowvar=False)

