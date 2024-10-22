MY_INFO = {}
Name = input("Enter Your Name: ")
Age = input("Enter YOur age: ")
Religion = input("Enter your religion: ")
Profession  = input("Enter you profession: ")
MY_INFO['Name'] = Name
MY_INFO['age'] = Age
MY_INFO['religion']  = Religion
MY_INFO['Profession'] = Profession
print(MY_INFO)
del MY_INFO['Name']
print(MY_INFO)