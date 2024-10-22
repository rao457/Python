import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 500)
y = np.abs(2*x + 1)

plt.plot(x, y, label=r'$y = |2x + 1|$', color='b')
# plt.figure(figsize=(6,6))
plt.xlabel("x")
plt.ylabel("Y")
plt.title("Graph of |2x + 1|")
plt.axvline(0, color='black', linewidth=2)
plt.axhline(0, color='black', linewidth=2)
plt.legend()
plt.show()