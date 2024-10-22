ALIEN_POSITION = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
ALIEN_POSITION['speed'] = 'fast'
print(f"Now Alien x_position is {ALIEN_POSITION['x_position']}")
if ALIEN_POSITION['speed'] == 'slow':
    x_increment = 1
elif ALIEN_POSITION['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
ALIEN_POSITION['x_position'] = ALIEN_POSITION['x_position'] + x_increment
print(f"Now Alien position is {ALIEN_POSITION['x_position']}")

