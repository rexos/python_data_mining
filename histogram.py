import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
data = ss.norm.rvs(loc=0,scale=2,size=10000, facecolor='b')**2
data = data + 10
plt.hist(data,100, normed=True)
x = np.linspace(0,20)
plt.plot(x, ss.norm.pdf(x,loc=10,scale=2), lw=5)
plt.show()
