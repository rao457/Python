import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 400)
y = 2 * x + x ** 2

# Plot the graph
plt.plot(x, y, label=r'$y = 2x + x^2$', color='b')
plt.title("Graph of $y= 2x + x^2$ on rectangular components")
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(0, color='black', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.xlim([-2, 5])
plt.ylim([-5, 5])
plt.legend()
plt.show()