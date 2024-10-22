def count_consonants_vowels(input_str):
    vowels = 'aeiou'
    vowels_count = 0
    consonants_count = 0
    for char in input_str:
        if char.lower() in vowels:
            vowels_count += 1
        elif char.isalpha():
            consonants_count += 1
    return {'Vowels' : vowels_count, 'Consonants' : consonants_count}
my_info = input("Who are You? ")
result = count_consonants_vowels(my_info)
print(result)
