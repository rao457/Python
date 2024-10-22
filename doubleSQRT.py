import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4, 400)
y = np.sqrt(2 - np.sqrt(x))

# plot the graph
plt.plot(x, y, label=r'$y = \sqrt{2 - \sqrt{x}}', color='b')
plt.title("Graph of $y= \sqrt{2 - sqrt{x}}$ on rectangular components")
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(0, color='black', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.legend()
plt.show()