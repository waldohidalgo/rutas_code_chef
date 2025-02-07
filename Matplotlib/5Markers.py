import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(6, 4))
plt.plot(x[::10], y1[::10], marker='o', label='Circle',linestyle='--',color='g')
plt.plot(x[::10], y1[::10] + 1, marker='s', label='Square',linestyle=':',color='b')
plt.plot(x[::10], y1[::10] + 2, marker='^', label='Triangle',linestyle='-',color='#FFA500')
plt.legend()
plt.title('Different Markers')
plt.show()