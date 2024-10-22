from operator import itemgetter,attrgetter
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]
from collections import Counter
words_count = Counter(words)
most_occuring = words_count.most_common(2)
print(most_occuring)
def dedupe(my_list): 
    seen = set()
    for item in my_list:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
def dict_dedupe(dic, key= None):
    seen = set()
    for item in dic:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dict_dedupe(a, key=itemgetter('y'))))
message = 'Assalam-o-Alaikum! This is message from fsociety don\'t leave your systems unsecure'
greet = slice(0, 18)
mess = slice(18, 60)
print(message[greet])
print(message[mess])
rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
class User:
    def __init__(self, uid):
        self.uid = uid
    def __repr__(self):
        return f"User {self.uid}"
users = [User(23), User(54), User(64), User(1), User(2),User(87), User(63)]
sorted_uids = sorted(users, key=attrgetter('uid'))
print(sorted_uids)
rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from itertools import groupby
rows.sort(key=itemgetter('date'))
for date, item in groupby(rows, key= itemgetter('date')):
    print(date)
    for i in item:
        print("     ",i)