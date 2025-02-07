import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a figure
fig = plt.figure(figsize=(12, 10))

# Create a 3D axes
ax = fig.add_subplot(111, projection='3d')

# Set labels for each axis
ax.set_xlabel('Time', fontsize=12)
ax.set_ylabel('Distance', fontsize=12)
ax.set_zlabel('Speed', fontsize=12)

# Set the viewing angle
ax.view_init(elev=30, azim=60)

# Add a title
ax.set_title('Vehicle Motion in 3D', fontsize=14)

# Optional: Add some dummy points to see the 3D effect
x = np.random.rand(20)
y = np.random.rand(20)
z = np.random.rand(20)
ax.scatter(x, y, z, c='b', marker='o')

# Show the plot
plt.show()