favourite_languages = {
    'zohaib': 'python',
    'sonia': 'c++',
    'shoaib': 'Java',
    'zubair': 'Klinton'
}
if 'Erin' not in favourite_languages.keys():
    print('Please, take our poll.')
friends = ['zohaib', 'zubair']
for name in sorted(favourite_languages.keys()):
    print(f"Hi {name.title()}")
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")