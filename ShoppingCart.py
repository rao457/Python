import os
path = os.path.join('window', 'usr', 'zohaib')
print(path)
myfiles = ['intro.txt', 'self.csv', 'you.docx']
for filename in myfiles:
    print(os.path.join(r'C:/Users', filename))
print(os.getcwd())
os.chdir(r"C:/Users")
print(os.getcwd())
os.chdir(r"C:/Users/Soul Drawer/Desktop/new")
print(os.getcwd())

    