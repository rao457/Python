def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    
    
    
items = [1,1,2,2,3,3,4,4,5,5]
print(list(dedupe(items)))
# For unhashable or not iterable objects we use following recipe
def dedupe_again(items, key= None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)
a = [{'x':1, 'y':2}, {'x': 1, 'y': 2}, {'x': 2, 'y': 1}, {'x': 3, 'y': 2}]
print(list(dedupe_again(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe_again(a, key= lambda d: d['y'])))

            
