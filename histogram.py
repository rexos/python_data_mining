import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
alpha, loc, beta=2, 10, 22
x = np.linspace(50,200, 500)
data = ss.norm.rvs(loc=0,scale=2,size=10000, facecolor='b')
data = data + 10
plt.hist(data,100, normed=True)
x = np.linspace(0,20)
plt.plot(x, ss.norm.pdf(x,loc=10,scale=2), lw=5)
plt.show()
