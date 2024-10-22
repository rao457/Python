a = [{'x':1, 'y':1}, {'x': 1, 'y':1 }, {'x': 2, 'y': 1}, {'x': 3, 'y':1}]
def deletedupe(list1, key = None):
    seen = set()
    for item in list1:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val) 
print(list(deletedupe(a, key = lambda d: (d['x'], d['y']))))