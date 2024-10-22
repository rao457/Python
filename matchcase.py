from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('csv4.txt', 'csv[1-4].txt'))
print(fnmatch('gibbrishzohaibgibbris', '*zohaib*'))
#Advanced Searches
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
found = [name for name in names if fnmatch(name,'Dat*.csv')]
print(found)
addresses = [ '5412 N CLARK ST',
 '1060 W ADDISON ST',
 '1039 W GRANVILLE AVE',
 '2122 N CLARK ST',
 '4802 N BROADWAY',]
found_addr = [addr for addr in addresses if fnmatch(addr, '54[1-9][1-9]*CLARK*')]
print(found_addr)