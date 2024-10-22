import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,400)
y = np.sqrt(4 - x**2)

# plot the graph
plt.plot(x, y, label=r'$y= \sqrt{4 - x^2}$', color='b')
plt.title("Graph of $y= \sqrt{4 - x^2}$ in rectangular components.")
plt.axvline(0, color="black", linewidth=1)
plt.axhline(0, color="black", linewidth=1)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.legend()
plt.show()