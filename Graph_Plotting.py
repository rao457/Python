from plotly.graph_objs import Bar
from plotly import offline

name = ['zohaib', 'shoaib', 'sonia', 'zubair', 'sadia', 'saba', 'javeria',
        'saifi', 'arshad', 'shahbaz']
numbers = [89,99,65,23,87,90,95,67,98,78]
data = [{
    'type': 'bar',
    'x' : name,
    'y' : numbers,
    'marker' : {
        'color' : 'rgb(25,25,25)',
        'line' : {'width' : 2.0, 'color': 'rgb(23,23,23)'},

    },
    'opacity' : 0.6,
}]
my_layout = {
    'title': 'Name and Numbers Graph',
    'xaxis' : {'title' : 'Name'},
    'yaxis' : {'title' : 'Numbers'},
    
    

}
fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='my_graph.html')

