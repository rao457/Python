def key_word(first, last, **kwargs):
    
    kwargs['First_Name'] = first
    kwargs['last_name'] = last
    return kwargs
    
kwargs = key_word('Roa', "Zohiab", religion =  'Islam', location = 'Pakistan')
print(kwargs) 
# ** two aistiks trigger making a dictionary in python actually an empty dictionary
