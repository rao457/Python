def duplicates_finder(org):
    mod = []
   
    for i in org:
        if (org.count(i*2)):
            mod.append(i)
    return sorted(mod)
org = [1, 2, 3, 1, 3, 4, 2, 5, 6, 5]
result = duplicates_finder(org)
print(result)