# This program is gonna remove duplicates the iterable objects preserving their original order
def sort_order(my_list):
    """ This program iterates over the given list and see if the item in the created
    set if not add item in the order it appears in the list"""
    seen = set()
    for item in my_list:
        if item not in seen:
            yield item
            seen.add(item)
my_list = [6,4,7,3,7,4,3,5]
print(list(sort_order(my_list)))