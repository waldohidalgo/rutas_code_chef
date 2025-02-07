import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
data = np.array([
    [5, 10, 15, 20, 25, 30, 32, 31, 26, 21, 15, 8],  # Year 2020
    [6, 11, 16, 21, 26, 31, 33, 32, 27, 22, 16, 9],  # Year 2021
    [4, 9, 14, 19, 24, 29, 31, 30, 25, 20, 14, 7]    # Year 2022
])

# Create a heatmap
plt.figure(figsize=(6, 4))
plt.imshow(np.transpose(data), cmap='viridis')

# Add colorbar
plt.colorbar()

# Add labels
plt.title('Simple Heatmap')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()