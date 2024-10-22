import heapq

list_of_dicts = [
    {'a': 1, 'b': 2},
    {'a': 3, 'b': 4},
    {'a': 5, 'b': 6},
    {'a': 7, 'b': 8},
    {'a': 9, 'b': 10}
]
largest = heapq.nlargest(1, list_of_dicts, key = lambda s : s ['a'])
print(largest)
portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, lambda s: s['price'])
print(cheap)
