prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
min_price = min(zip(prices.keys(), prices.values()))
print(min_price)
max_price = max(zip(prices.keys(), prices.values()))
print(max_price)
num = 1
for key, value in prices.items():
	print(f"{num}-{key}  :  {value}")
	num += 1

sorted_prices = sorted(zip(prices.values(),prices.keys()))
print(sorted_prices)
min_key = min(prices, key = lambda k: prices[k])
print(min_key)
max_key = prices[max(prices, key = lambda k: prices[k])]
print(max_key)