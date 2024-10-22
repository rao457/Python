class Rectangle:
    """ This class defines rectangle's width and length and then eventually calculate the area and perimeter"""
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area_perimeter(self, args):
        if args == 'area':
            area = self.length * self.width
            return area
        elif args == 'perimeter':
            perimeter = 2 * (self.width + self.length)
            return perimeter

my_rectangle = Rectangle(20, 30)
ask_user = input("What do you want to calculate (area / perimeter)? ")

if ask_user == 'area':
    print(my_rectangle.area_perimeter('area'))
elif ask_user == 'perimeter':
    print(my_rectangle.area_perimeter('perimeter'))
else:
    print("Invalid input. Please enter 'area' or 'perimeter'.")




class Rectangle:
    """ This class defines rectangle's width and length and then eventually calculate the area and perimeter"""
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.width + self.length)

            
my_rectangle = Rectangle(20, 30)
result1 =my_rectangle.area()
print(f"Area of rectangle is {result1}")
result2 = my_rectangle.perimeter()
print(f"Perimeter of rectangle is {result2}")