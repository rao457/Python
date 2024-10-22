def square(n):
    return n*n

# f = square
# print(f(5))
def my_map(func, num_list):
    result = []
    for i in num_list:
        result.append(func(i))
    return result
num_list = [1,2,3,4,5]
f = my_map(square, num_list)
print(f)
def logger(msg):
    def log_msg():
        print('Hi', msg)
    return log_msg
var = logger('Zohaib')
var()
def htl_tag(tag):
    def my_heading(msg):
        print(f"<{tag}>{msg}</{tag}>")
    return my_heading
print_tag = htl_tag("h2")
print_tag("My Heading")
print_tag("Another Heading")

