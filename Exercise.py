from tkinter import *
def entries(x,y):
    return x+y


window = Tk()
window.geometry('400x400')
window.configure(background='white')
entry1 = Entry(window, highlightbackground='cyan', highlightthickness=2)
entry1.place(x=20, y=20)
entry2 = Entry(window, highlightbackground='cyan', highlightthickness=2)
entry2.place(x= 20, y=70)
def result2():
    result = entries(entry1, entry2)
    return result
calculate = Button(window, text='calculate', font=('Ivy 10 italic'), fg='cyan', command=result2)
calculate.place(x=10, y=100)
window.mainloop()

