count = {}
def word_count():
    TAKE = input("Enter something: ")
    words = TAKE.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

result=word_count()
print(result)