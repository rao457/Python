alien = {'name': 'zapada', 'speed': 'medium', 'x_position' : 0}
if alien['speed'] == 'slow':
    x_increment = 5
elif alien['speed'] == 'medium':
    x_increment = 10
elif alien['speed'] == 'fast':
    x_increment = 15
alien['x_position'] = alien['x_position'] + x_increment 
print(f"New alien position is {alien['x_position']}")