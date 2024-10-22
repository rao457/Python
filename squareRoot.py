import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(5, 15, 400)
y = np.sqrt(x - 5)

# Let's plot it
plt.plot(x, y, label = r'$y = \sqrt{x - 5}$', color='b')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of $y = \sqrt{x - 5}$ in Rectangular components")
plt.axvline(0, color='black', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.xlim([5, 15])
plt.ylim([0, 10])
plt.legend()
plt.show()