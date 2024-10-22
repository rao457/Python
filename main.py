from tkinter import Tk, Canvas
from PIL import Image, ImageTk

# Open the image using PIL
image = Image.open("image.jpeg")

# Create a Tkinter window
root = Tk()
root.title("Image Positioning")

# Create a canvas to display the image
canvas = Canvas(root, width=image.width, height=image.height)
canvas.pack()

# Convert the PIL image to a Tkinter PhotoImage
photo_image = ImageTk.PhotoImage(image)

# Position the image at coordinates (x, y)
x = 50
y = 50
canvas.create_image(x, y, image=photo_image, anchor='nw')  # 'nw' means northwest corner

root.mainloop()
