import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 800)
y = x**2 - 2* x + 1

# lets plot
plt.plot(x, y, label=r'$y = x^2 - 2x + 1$')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of $y = x^2 - 2x + 1$ in Rectangular Plane")
plt.grid(True)
plt.axvline(0, color="black", linewidth=1)
plt.axhline(0, color="black", linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()