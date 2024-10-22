my_cont = {}

str = input(">")

def count_vowels(str):
    
    alpha = 0
    elpha = 0
    ilpha = 0
    olpha = 0
    ulpha = 0
    
    if 'a' in str:
        alpha = str.count('a')
    if 'e' in str:
        elpha = str.count('e')
    if 'i' in str:
        ilpha = str.count('i')
    if 'o' in str:
        olpha = str.count('o')
    if 'u' in str:
        ulpha = str.count('u')
    all_v = alpha+elpha+ilpha+olpha+ulpha
    return all_v

my_vowels = count_vowels(str)

my_cont['Vowels'] = my_vowels

def count_consonants(str):
    str = ''.join(str.split())
    consonants = len(str) - my_vowels
    return consonants

my_cont['Consonants'] = count_consonants(str)
print(my_cont)
