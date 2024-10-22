from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Test File", "*.txt")])
    if not filepath:
        return
    text_edit.delete(1.0, END)
    with open(filepath, 'r') as f:
        content = f.read()
        text_edit.insert(END, content)
    window.title(f"Open File: {filepath}")
def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Test File", "*.txt")])
    if not filepath:
        return
    with open(filepath, 'w') as f:
        content= text_edit.get(1.0, END)
        f.write(content)
    window.title(f"Open File: {filepath}")


def main():
    window = Tk()
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)
    window.title('Text Editor')
    text_edit = Text(window, autoseparators=True, font='Helvetica 20 bold' )
    text_edit.grid(row=0, column=1, padx=10)
#SCROLL BAR
    scrollbar = Scrollbar(window, command=text_edit.yview)
    scrollbar.grid(row=0, column=2, sticky="ns")
    text_edit.config(yscrollcommand=scrollbar.set)
#FRAME 
    BUTTONS_FRAME = Frame(window, relief=RAISED, bd=2, highlightthickness=3, highlightbackground='cyan', height=50, width=50)
    open_button = Button(BUTTONS_FRAME, text='Open', font=('Ivy 10 bold'), command= lambda: open_file(window, text_edit ))
    open_button.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    save_button = Button(BUTTONS_FRAME, text='Save', font=('Ivy 10 bold'), command= lambda: save_file(window, text_edit ))
    save_button.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
    BUTTONS_FRAME.grid(row=0, column=0, sticky='ns')
    window.mainloop()
main()