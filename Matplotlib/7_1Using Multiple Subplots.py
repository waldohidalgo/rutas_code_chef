import matplotlib.pyplot as plt
import numpy as np

# Create a figure with 1 row and 2 columns of subplots
fig, axs = plt.subplots(2, 2, figsize=(6, 4))

# Generate x values from 0 to 10 with 100 points
x = np.linspace(0, 10, 100)
data = np.random.uniform(0,10,100)

# Plot sine function on the first subplot
axs[0][0].plot(x, np.sin(x))
axs[0][0].set_title('Sine Wave')

# Plot tangent function on the second subplot
axs[0][1].plot(x, np.tan(x))
axs[0][1].set_title('Cosine Wave')

axs[1][0].scatter(x, data)
axs[1][0].set_title('Scatter Plot')

axs[1][1].hist(data)
axs[1][1].set_title('Histogram')

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()