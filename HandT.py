import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 400)
y = 4 - x**2 / (2 - x)

plt.plot(x, y, label=r'$y = 4 - x^2 / (2 - x)$', color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of $y = 4 - x^2 / (2 - x)$ in Rectrangular components")
plt.axvline(0, color='black', linewidth= 1, linestyle="solid")
plt.axhline(0, color='black', linewidth= 1, linestyle="solid")
plt.gca().set_aspect('equal', adjustable='datalim')
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.legend()
plt.show()