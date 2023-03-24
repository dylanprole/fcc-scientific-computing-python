# Code to calculate the internal area of a polygon
# Replit link: https://replit.com/@dylanprole/boilerplate-polygon-area-calculator

# Parent class
class Rectangle:
    polygon = 'rectangle'

    # Construct Rectangle object
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
    
    # Set a new width for the polygon
    def set_width(self, new_width):
        self.width = int(new_width)

        # Set height if polygon is a square
        if self.polygon == 'square':
            self.side = self.width
            self.height = self.width

    # Set a new height for the polygon
    def set_height(self, new_height):
        self.height = int(new_height)

        # Set width if polygon is a square
        if self.polygon == 'square':
            self.side = self.height
            self.width = self.height

    # Get width for the polygon
    def get_width(self):
        return self.width

    # Get height for the polygon
    def get_height(self):
        return self.height

    # Get the area of the polygon
    def get_area(self):
        return self.width * self.height
    
    # Get the length of the perimiter of the polygon
    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    # Get the diagonal length of the polygon
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    # Method to print out a visual representation of the polygon
    def get_picture(self):
        if max([self.width, self.height]) >= 50:
            return 'Too big for picture.'
        
        # Return string of polygon made from asterisks
        picture = ''
        for i in range(self.height):
            picture += '*' * self.width + '\n'

        return picture

    def get_amount_inside(self, polygon):
        # Find number of times the width of the smaller polygon
        # could fit into the larger polygon
        fit_width = int(self.width//polygon.width)

        # Find number of times the height of the smaller polygon
        # could fit into the larger polygon
        fit_height = int(self.height//polygon.height)

        # Return number of times the smaller polygon could fit
        # into the larger polygon
        return int(fit_width * fit_height)

    # String returned when calling print()
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

# Child class
class Square(Rectangle):
    polygon = 'square'

    # Consctruct Square object and inherit all methods from Rectangle class
    def __init__(self, side):
        super().__init__(side, side)
        self.side = int(side)

    # Set a new side length for the square object
    def set_side(self, new_side):
        self.side = int(new_side)
        self.width = self.side
        self.height = self.side

    # Get the diagonal length of the sqaure object
    def get_diagonal(self):
        return (2*(self.side**2))**0.5
    
    # String returned when calling print()
    def __str__(self):
        return f'Square(side={self.side})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(2)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

print('Rectangle width =', rect.get_width())
print('Rectangle height =', rect.get_height())
print('Square width =', sq.get_width())
print('Sqaure height =', sq.get_height())

print(rect.get_amount_inside(sq))

sq.set_width(4)

print('Square width =', sq.get_width())
print('Sqaure height =', sq.get_height())


sq.set_height(6)

print('Square width =', sq.get_width())
print('Sqaure height =', sq.get_height())

# 50
# 26
# Rectangle(width=10, height=3)
# **********
# **********
# **********

# 81
# 5.656854249492381
# Square(side=4)
# ****
# ****
# ****
# ****

# 8