def word_frequency(text):
    
    from collections import Counter
    text = "Hello world! This is a python challenge. Can you solve it? I hope so!"
    text = text.replace('!', '').lower()
    text = text.split(' ')
    word_count =  Counter(text)
    return word_count
text = "Hello world! This is a python challenge. Can you solve it? I hope so!"
print(word_frequency(text))