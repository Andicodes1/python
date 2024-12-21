class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello , I am {self.name} and I am {self.age} years old")

person1 = Person (name="Andi" , age=25)
person2 = Person (name="Camavinga" , age=23)


person1.greet()
person2.greet()