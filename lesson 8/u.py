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




# class Animal:
#     def __init__(self):
#         self.name = name

#     def make_sound(self):

# # Child class for Dog
# class Dog(Animal):
#     def make_sound(self):
#         return f"{self} says: Woof Woof!"

# # Child class for Cat
# class Cat(Animal):
#     def make_sound(self):
#         return f"{self} says: Meow!"

# # Call the make_sound method for each animal
# print(dog.make_sound())  # Output: Buddy says: Woof Woof!
# print(cat.make_sound())  # Output: Whiskers says: Meow!

class Vehicle:
def __init__(self, make, model, year): 
self.make = make
self.model = model
self.year = year
def display_info(self): 
new *
print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}") I

class Car(Vehicle): 
def __init__(self, make, model, year, body_style): 
super().__init__(make, model, year)
self.body_style = body_style


class ElectricCar (Car): 
def __init__(self, make, model, year, body_style, battery_capacity): 
 super().__init__(make, model, year, body_style) self.battery_capacity = battery_capacity


def charge (self): 
print("charging the battery of electric car!")
tesla = ElectricCar( make: "Tesla", model: "Cybertruck", year: 2024, body_style: "SQUARE", battery_capacity: 350)

string_length = len("Hello World")
list_length = len([1, 2, 3, 4, 5, 6, 7, 8])
tuple_length = len((10,20,30))

print(string_length)
print(list_length)
print(tuple_length)
