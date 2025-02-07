import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 3, figsize=(6, 6))

x = np.linspace(-np.pi, np.pi, 100)

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Sine')

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('Cosine')

axs[1, 0].plot(x, np.tan(x))
axs[1, 0].set_title('Tangent')

axs[1, 1].plot(x, np.arcsin(x))
axs[1, 1].set_title('Arcsine')

plt.tight_layout()
plt.show()