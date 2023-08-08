import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

y = x ** (1 / 3)

plt.plot(x, y)
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.grid(True)
plt.show()