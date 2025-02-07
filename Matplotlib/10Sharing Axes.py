import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 2, figsize=(6, 4), sharey=True)

x = np.linspace(0, 10, 100)

ax[0].plot(x, np.power(x,2),color="red")
ax[0].set_title('Square')

ax[1].plot(x, np.power(x,3),color="blue")
ax[1].set_title('Cubic')

plt.xlabel('x')
plt.tight_layout()
plt.show()