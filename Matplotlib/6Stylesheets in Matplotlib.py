import matplotlib.pyplot as plt
import numpy as np

plt.style.use(['seaborn', 'dark_background'])
# 'default': The default Matplotlib style
# 'classic': The classic Matplotlib style
# 'seaborn': A more modern, visually pleasing style
# 'ggplot': Mimics the aesthetics of ggplot in R
# 'bmh': A style inspired by the Bayesian Methods for Hackers book
# 'dark_background': A style with a dark background, useful for presentations
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.title('Sine Wave')
plt.show()