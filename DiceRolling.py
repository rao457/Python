import random
class Dice:
    """ This is fun class to keep record of rolling dice in the class"""
    def __init__(self):
        self.sides = 6
    def roll_dice(self):
        side = random.randint(1, 6)
        return side
my_dice = Dice()
up_side = my_dice.roll_dice()
print(f"Yeeeeah Now I got {up_side} side up.")