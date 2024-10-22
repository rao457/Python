""" We can bring out any sequence of number within a huge 
file with this method it matching with regular expression"""
import re
with open('phonenumber.txt', 'r', encoding='utf-8') as file_object:
    content = file_object.read()
phoneNumber = re.compile(r'(\d\d\d\d)-(\d\d\d\d-\d\d\d\d\d\d\d)')
mo = phoneNumber.search(content)
areacode, phonenumber = mo.groups()
print(areacode)
print(phonenumber)