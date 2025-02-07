import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(10)
group1 = np.random.normal(100, 10, 200)
group2 = np.random.normal(80, 30, 200)
group3 = np.random.gamma(5, 10, 200)

# Create violin plot
fig, ax = plt.subplots(figsize=(6, 4))
violin_parts = ax.violinplot([group1, group2, group3])


plt.show()