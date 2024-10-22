import re
PhoneNumber = re.compile(r'(\d\d\d\d)(-)(\d\d\d\d\d\d\d)')
mo = PhoneNumber.search('My phone number is 0304-9011792.')
found, hyphen, found_again = mo.groups()
print(found,hyphen,found_again)

Hero = re.compile(r'Zohaib|Shoaib')
mo_1 = Hero.search("My name is Zohaib, and my brother is Shoaib")
print('I am ' +  mo_1.group()) 
mo_2 = Hero.search('My name is Zohaib, and my brother is Shoaib')
print(mo_2.group())