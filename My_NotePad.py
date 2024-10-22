it_list = []
for new_dict in range(10):
    my_dict = {
        'name' : 'zohaib',
        'age' : 20,
        'profession': 'hacker',
        'speciality' : 'intelligence',
        'experience': 'Army, computer Science, SEO'
    }
    it_list.append(my_dict)
for dict in it_list[:5]:
    dict['name'] = 'shoaib',
    dict['profession'] = 'mason',
    dict['speciality'] = 'Clean',
    dict['experience'] = 'money'
print(it_list)