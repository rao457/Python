import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 400)
y = np.sqrt(x**4)

plt.plot(x, y, label=r'$y= \sqrt{x^4}$', color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(0, color='black', linewidth=2)
plt.axhline(0, color='black', linewidth=2)
plt.title("Graph of $y = \sqrt{x^4}$")
plt.legend()
plt.xlim([-4, 4])
plt.ylim([-10, 10])
plt.show()