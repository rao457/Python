import numpy as np
import matplotlib.pyplot as plt

# Define the function and values for plotting
x = np.linspace(-10, 10, 400)

y = 2 + x

# Plot the graph
plt.plot(x, y, label=r'$y = 2 + x$')

# Correct title with proper LaTeX formatting
plt.title(r"Graph of $y = 2 + x$ on rectangular components")

plt.axvline(0, color='black', linewidth=1)  # y-axis
plt.axhline(0, color='black', linewidth=1)  # x-axis
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.xlim([-10, 10])
plt.ylim([-10, 10])
# Show the plot
plt.show()
