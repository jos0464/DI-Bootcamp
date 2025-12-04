import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 1
data = np.random.normal(mu, sigma, 1000)
plt.hist(data, bins=30)
plt.show()

