import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 10, 400)
y = np.sqrt(x + 2)
# plot the graph
plt.plot(x, y, label=r'$y= \sqrt{x + 2}$', color='b')
plt.title("Graph of the $y= \sqrt{x + 2}$ on rectangular components")
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(0, color='black',linewidth=1)
plt.axhline(0, color='black',linewidth=1)
plt.xlim([-2, 10])
plt.ylim([-10, 10])
plt.legend()
plt.show()

