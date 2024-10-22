from tkinter import *
from PIL import Image, ImageTk
def main():
    window = Tk()
    window.title('Image')
    image = Image.open('C:/Users/Soul Drawer/Downloads/Documents/sir/Sir/ustad_g.jpeg')
    tk_image = ImageTk.PhotoImage(image)
    label = Label(window, image = tk_image)
    label.pack()
    window.mainloop()
if __name__=='__main__':
    main()