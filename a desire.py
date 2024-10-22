from tkinter import *

def add(x, y):
    a = int(x) + int(y)
    return a

def window():
    scr = Tk()
    scr.configure(background='white')
    scr.geometry('400x400')
#Button
    entry_1 = Entry(scr, highlightbackground='cyan', highlightthickness=2)
    entry_1.grid(row=1, column=0, padx=20, pady=20)
    entry_2 = Entry(scr,highlightbackground='cyan', highlightthickness=2, command = add(entry_1.get, entry_2.get))
    entry_2.grid(row=2, column=0, padx=20, pady=20)
    calculate = Button(scr, text="calculate", highlightbackground='cyan', fg='black')
    calculate.grid(row=3, column=0, padx=20, pady=20)
    scr.mainloop()

window()
