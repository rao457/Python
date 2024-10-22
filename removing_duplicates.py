def dedpe(my_list):
	seen = set()
	for item in my_list:
		if item not in seen:
			yield item
			seen.add(item)
my_list = [1,2,2,4,5,6,7,4,1]
print(list(dedpe(my_list)))