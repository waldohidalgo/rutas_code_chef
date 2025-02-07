import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.stats import truncnorm


mu, sigma = 5, 2  
lower, upper = 0, 10  


a, b = (lower - mu) / sigma, (upper - mu) / sigma 
samples = truncnorm.rvs(a, b, loc=mu, scale=sigma, size=500)

x = samples
y = np.sqrt(x)
z = np.log(x)

# Create the 3D scatter plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create scatter plot with color-coding and size variation
scatter = ax.scatter(x, y, z, c=z, cmap='viridis', alpha=0.6)

# Set the viewing angle
ax.view_init(elev=20, azim=45)

plt.show()