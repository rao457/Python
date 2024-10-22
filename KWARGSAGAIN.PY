def key_arguments(job_post, name, **employee):
    employee['Name'] = name
    employee['Job_Post'] = job_post
    return employee
result = key_arguments('Hacker', 'Zohaib', age = 20, religion = 'Islam', Location = 'Pakistan')
print(result)