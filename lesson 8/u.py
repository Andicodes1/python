class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance of Rectangle
my_Rectangle = Rectangle(length=5, width=3)

# Call methods to calculate area and perimeter
area = my_Rectangle.calculate_area()
perimeter = my_Rectangle.calculate_perimeter()

# Output the results
print(f"Area is: {area}")
print(f"Perimeter is: {perimeter}")
