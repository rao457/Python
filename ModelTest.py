import matplotlib.pyplot as plt
import numpy as np
x = np.array([1000, 1500, 2000, 2500, 3000,35000])
y = np.array([300000, 450000, 600000, 750000, 900000, 472500])

plt.plot(x, y)
plt.title("Model Test")
plt.xlabel("Size of the house")
plt.ylabel("Cost of the house")
plt.axvline(0, color='black', linewidth=1)
plt.axhline(0, color='black', linewidth=1)
plt.show()