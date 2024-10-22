# Test graph is right
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(4, -4, 100)
y = 2 * x - x*x

plt.plot(x, y, label=r'$y = 2*x - x^2$', color='b')
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)
plt.xlim([-2, 2])
plt.ylim([-5, 5])
plt.show()
