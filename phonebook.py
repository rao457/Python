from tkinter import *
from tkinter import ttk
WHITE = '#ffffff'
BLACK = '#000000'
BLUE = '#4456f0'
window = Tk()
window.title("PhoneBook")
window.geometry("500x470")
window.configure(background=WHITE)
window.resizable(width= False, height= False)

#FRAMES
frame_up = Frame(window, width= 500, height= 45, bg=BLUE)
frame_up.grid(row=1, column=0, padx = 0, pady= 10)
frame_down = Frame(window, width=500, height= 150, bg = WHITE)
frame_down.grid(row=2, column=0, pady= 0, padx = 0)
#FRAME_TABLE
frame_table = Frame(window, width = 500, height=100, bg= WHITE)
frame_table.grid(row= 3, column=0, columnspan=2, padx=0, pady= 1, sticky=NW)
#FUNCTIONS
def show():
    global tree
    list_headers = ['Name', 'Gender', 'Telephone', 'Email']
    tree = ttk.Treeview(frame_table, selectmode=EXTENDED, columns= list_headers, show = 'headings')
    VSB = ttk.Scrollbar(frame_table, orient=VERTICAL, command=tree.yview)
    HSB = ttk.Scrollbar(frame_table, orient = HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand= VSB.set, xscrollcommand= HSB.set)
    tree.grid(column= 0, row=0, sticky= 'nsew')
    VSB.grid(column= 1, row=0, sticky = 'ns')
    HSB.grid(column=0, row = 1, sticky = 'ew')
    #TREE HEADER
    tree.heading(0, text='Name', anchor=NW)
    tree.headig(1, text = 'Gender', anchor = NW)
    tree.heading(2, text= 'Telephone', anchor = NW)
    tree.heading(3, text = 'Email', anchor = NW)
    #TREE COLUMNS 
    tree.column(0, width = 120, anchor='nw')
    tree.column(1, width = 50, anchor='nw')
    tree.column(2, width = 100, anchor='nw')
    tree.column(3, width = 180, anchor='nw')



    show()
# FRAME_UP WIDGETS
label = Label(frame_up, text="Phonebook", font= ('Verdana 17 bold'), bg= BLUE,  fg = WHITE)
label.place(x= 5, y= 5)
# FRAME_DOWN WIDGETS
#NAME
NAME = Label(frame_down, text= "Name* ", width= 20, height=1 , font= ('Ivy 10'), anchor = NW, bg=WHITE)
NAME.place(x=20, y=1)
ENTRY = Entry(frame_down, width = 25, highlightthickness=2, justify= 'left', relief='groove' )
ENTRY.place(x=70, y=1)
#NUMBER
NUMBER = Label(frame_down, text= "Ph Number", width = 20, height= 1 , font= ('Ivy 10'), anchor= NW)
NUMBER.place(x=20, y=50)
NUM_ENTRY = Entry(frame_down, width= 25  , highlightthickness= 2, relief='groove', justify='left')
NUM_ENTRY.place(x=70, y= 50)
#GENDER
GENDER = Label(frame_down, text= "Gender", width = 20, height= 1, font=('Ivy 10'), anchor = NW)
GENDER.place(x=20, y=25)
GENDER_BOX = ttk.Combobox(frame_down, width = 25)
GENDER_BOX['values']= ['"', 'Female', 'Male']
GENDER_BOX.place(x=70, y=25)
#E-MAIL
E_MAIL = Label(frame_down, text = "E-Mail", width = 20, height=1, font = ('Ivy 10'), anchor= NW )
E_MAIL.place(x = 20, y= 75)
E_MAIL_ENTRY = Entry(frame_down, width = 25, highlightthickness=2 , justify='left', relief='sunken')
E_MAIL_ENTRY.place(x= 70, y= 75)
#SEARCH-BUTTON
SEARCH_BUTTON = Button(frame_down, height=1, width = 10, text = 'Search', font= ('Ivy 8 bold'), fg= WHITE, bg=BLUE)
SEARCH_BUTTON.place(x=250, y=25)
S_BUTTON_ENTRY = Entry(frame_down, width= 25, highlightthickness=2, relief='groove', justify='left')
S_BUTTON_ENTRY.place(x=335, y=25)
#VIEW BUTTON
VIEW_BUTTON = Button(frame_down, text = "View", height=1, width = 10, fg=WHITE, bg = BLUE, font= ('Ivy 8 bold'))
VIEW_BUTTON.place(x= 250, y= 55 )
#ADD BUTTON
ADD_BUTTON = Button(frame_down, text = "Add", height = 1, width = 10, font = ('Ivy 10 bold'), bg= BLUE, fg= WHITE)
ADD_BUTTON.place(x=400, y = 55)
#UPDATE BUTTON
UPDATE_BUTTON = Button(frame_down, text = 'Update', height = 1, width = 10, bg = BLUE, fg = WHITE, font = ('Ivy 10 bold'))
UPDATE_BUTTON.place(x=400, y = 85 )
#DELETE BUTTON
DELETE_BUTTON = Button(frame_down, text = 'Delete', height = 1, width = 10, fg= WHITE, bg= BLUE, font = ('Ivy 10 bold'))
DELETE_BUTTON.place(x=400, y = 115)
window.mainloop()
