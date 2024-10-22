from tkinter import *
from PIL import Image, ImageTk
def main():
    window = Tk()
    window.title('Image')
    window.geometry('400x400')
    my_image = Image.open('c:/Users/Soul Drawer/Desktop/me.jpg')
    tk_image = ImageTk.PhotoImage(my_image)
    label = Label(window, my_image=tk_image)
    label.pack()
    window.mainloop()
main()