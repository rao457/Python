import matplotlib.pyplot as plt
import numpy as np

# Generate x values, starting from a small positive number to avoid division by zero
x = np.linspace(0.001, 10, 400)

# Define the function
y = (3 * x + np.abs(x)) / x

# Plotting the graph
plt.plot(x, y, color='blue', label=r'$y = \frac{3x + |x|}{x}$')

# Adding labels, title, and axes
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of $y = \frac{3x + |x|}{x}$")
plt.axvline(0, color='black', linewidth=1)  # y-axis
plt.axhline(0, color='black', linewidth=1)  # x-axis
plt.xlim([0, 10])  # Adjust x-limits to match the x range
plt.ylim([3, 5])   # Adjust y-limits to match the expected y range
plt.legend()

# Show the plot
plt.grid()
plt.show()
