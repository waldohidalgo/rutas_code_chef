import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(0)
x = np.random.rand(100)*10
y = x+np.random.rand(100)

plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='blue', alpha=0.5)
plt.title('Random Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()