cont = {}
def words_frequency():
    TAKE = input("Etner something: ")
    take = TAKE.split()
    for word in take:
        word = word.lower()
        cont[word] = cont.get(word, 0) + 1
    return cont
result = words_frequency()
print(result)
