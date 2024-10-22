import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = 2 - 0.4 * x
 # plot the graph

plt.plot(x, y, label = r'$y= 2 - 0.4 * x', color='b')
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(0, color="black", linewidth=1)
plt.axhline(0, color="black", linewidth=1)
plt.axvline(x=5, color='red', linewidth=1, linestyle='dashed')
plt.title("Graph of $y = 2 - 0.4 *  x$ on rectangular componenets")
plt.legend()
plt.show()