import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.figure(figsize=(6,7))
plt.plot(x,y, label="Simple line graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.axvline(x=3, color='red', linestyle='--', linewidth=3, label="x = 3")
plt.axhline(y=4, color='blue', linestyle="dotted", linewidth=2, label="y = 4")
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
