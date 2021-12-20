import numpy as np
a3 = np.loadtxt("data/iris.csv", skiprows=1, usecols=(0, 1, 2, 3), delimiter=',')
print(np.mean(a3, axis=0), np.median(a3, axis=0), np.std(a3, axis=0))
