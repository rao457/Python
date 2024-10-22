from tkinter import *

def create_button(text, row, column, command=None):
    return Button(window, text=text, font=('Arial', 18, 'bold'), width=3, height=1, fg='white', bg='grey', command=command).grid(row=row, column=column, padx=5, pady=5)

def add_to_screen(text):
    screen.insert(END, text)

def clear_screen():
    screen.delete(1.0, END)

def calculate():
    try:
        result = eval(screen.get(1.0, END))
        clear_screen()
        add_to_screen(result)
    except Exception as e:
        clear_screen()
        add_to_screen("Error")

window = Tk()
window.geometry('500x500')
window.title("Calculator")
window.resizable(height=False, width=False)

# Frames
frame_title = Frame(window, height=75, width=500, bg='white')
frame_title.grid(row=0, column=0, padx=1, pady=1)
title_label = Label(frame_title, text="Calculator", font=('Arial', 25, 'bold'), fg='white', bg='grey')
title_label.grid(row=0, column=0, padx=5, pady=5)

screen = Text(window, font=('Arial', 18, 'bold'), height=2, width=30, bg='grey')
screen.grid(row=1, column=0, padx=2, pady=2, columnspan=4)

# Buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('+', 5, 3)
]

for button_text, row, column in buttons:
    if button_text == 'C':
        create_button(button_text, row, column, clear_screen)
    elif button_text == '=':
        create_button(button_text, row, column, calculate)
    else:
        create_button(button_text, row, column, lambda button_text=button_text: add_to_screen(button_text))

window.mainloop()
