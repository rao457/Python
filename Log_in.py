from tkinter import *


window = Tk()
window.geometry('600x400')
window.configure(background='cyan')
window.title('Log in page')
    
#Frame 
HEAD = Frame(window, bg='white', height=100, width=580)
HEAD.grid(row=0, column=0, padx=10, pady=10)
#Labels
HEAD_LABEL = Label(HEAD, text='Log In Page', fg='cyan', font=('Ivy 30 bold'))
HEAD_LABEL.place(x=10, y=10)
N_P_FRAME = Frame(window, height=120, width=580, bg='cyan')
N_P_FRAME.grid(row=1, column=0, padx=10, pady=10)
NAME_LABEL = Label(N_P_FRAME, text='Name', fg='WHITE', bg='cyan', font=('Arial 15 bold'))
NAME_LABEL.grid(row=0, column=0)
PASSWORD_LABEL = Label(N_P_FRAME, text='Password', font=('Arial 15 bold'), fg='white', bg='cyan')
PASSWORD_LABEL.grid(row=1, column=0)
LOG_BUTTON_FRAME = Frame(window, height=50, width=80, bg='white')
LOG_BUTTON_FRAME.grid(row=2, column=0, padx=10, pady=10)
#ENTRIES
ENTRY_1 = Entry(N_P_FRAME, highlightbackground='cyan', highlightthickness=2)
ENTRY_1.grid(row=0, column=1, padx=10, pady=10)
ENTRY_2 = Entry(N_P_FRAME, highlightbackground='cyan', highlightthickness=2)
ENTRY_2.grid(row=1, column=1, padx=10, pady=10)

def check_login():
    
    if (ENTRY_1.get().lower()=='zohaib') and (ENTRY_2.get().lower()=='xijinping090'):
        screen = Tk()
        screen.geometry('400x400')
        screen.configure(background='green')
        
        A_G_LABEL = Label(screen, text="***Access Granted***", font=('Arial 25 bold'),bg = 'green', fg='white')
        A_G_LABEL.grid(row=0, column=0, padx=50, pady=160)
        screen.mainloop()
    else:
        src = Tk()
        src.geometry('400x400')
        src.configure(background='red')
        
        A_G_LABEL = Label(src, text="***Access Denied***", font=('Arial 25 bold'),bg = 'red', fg='white')
        A_G_LABEL.grid(row=0, column=0, padx=50, pady=160)
        src.mainloop()
            
        # HEAD.place(x=10, y=10)
LOG_IN = Button(LOG_BUTTON_FRAME, text='Log In', fg='cyan', font=('Ivy 10 bold'), command= check_login)
LOG_IN.grid(row=0, column=0, padx=2, pady=2)

window.mainloop()

