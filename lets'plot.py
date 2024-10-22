import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,2, 400)
y = np.sqrt(4 - x**2)

# Let's plot it
plt.plot(x, y, label=r'$y = \sqrt{4 - x^2}$', color='b')
plt.title('Graph of $y = \sqrt{4 - x^2}$ in Rectangular Plane')
plt.grid(True)
plt.axvline(0, color='black', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.xlim([-2.5, 2.5])
plt.ylim([0, 4])
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()