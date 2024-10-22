word_count = {}
def count_it():
    ASK = input("Enter something: ")
    words = ASK.split()
    for word in words:
        word = word.lower()
        word = word.rstrip('!@$%^&*()_+|')
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
result = count_it()
print(result)