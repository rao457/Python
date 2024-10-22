string = ["apple", 'grapes', 'pineapple', 'apple', 'banana',
'grapes', 'apple', 'banana', 'apple']
from collections import Counter
word_count = Counter(string)
print(word_count.most_common(1))