from plotly.graph_objs import Bar
import random
from plotly import offline
numbers = []
name = ['zohaib', 'shoaib', 'sonia', 'zubair', 'sadia', 'saba', 'javeria',
        'saifi', 'arshad', 'shahbaz']

for num in range(random.randint(0,10)):
    numbers.append(num)
data = [{
    'type' : 'bar',
    'x' : name,
    'y' : numbers
}]
my_layout = {
    'title' : 'Names and number Graph',
    'xaxis' : {'title' : 'Names'},
    'yaxis' : {'title': 'Numbers'}
}
fig = {"data" : data, 'layout' : my_layout}
offline.plot(fig, filename = 'graph.html')


