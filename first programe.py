person_info = {
    'name' : 'zohaib',
    'hobbies' : ['golf', 'coding', 'hacking']
}

print(f"The suspect name is {person_info['name']} and his hobbies are as follows.")
for i, hobby in enumerate (person_info['hobbies'], start=1):

    print(f"\t {i}. {hobby}")
favourite_languages = {
    'zohaib' : ['python', 'html', 'java'],
    'sonia' : ['c', 'c++', 'kotlin'],
    'zubair' : ['react', 'javascript', 'css'], 
    'shoaib' : ['go', 'kotlin']

}
for person, language in favourite_languages.items():
    print(f"Hey {person.title()}, you like following languages: ")
    for i, language in enumerate (favourite_languages[person], start=1):
        print(f"\t {i}. {language}")