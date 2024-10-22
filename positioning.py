import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image Positioning")

# Load the image using Pillow
image_path = "C:/Users/Soul Drawer/Downloads/Documents/sir/Sir/ustad_g.jpeg"
original_image = Image.open(image_path)

# Resize the image if needed
# new_size = (width, height)
# original_image = original_image.resize(new_size, Image.ANTIALIAS)

# Create a Tkinter-compatible photo image
tk_image = ImageTk.PhotoImage(original_image)

# Create a Canvas widget to display the image
canvas = tk.Canvas(root, width= 600, height=1000)
canvas.pack()

# Position the image at coordinates (x, y)
x_position = 0
y_position = 0
canvas.create_image(x_position, y_position, anchor=tk.NW, image=tk_image)

# Run the Tkinter main loop
root.mainloop()