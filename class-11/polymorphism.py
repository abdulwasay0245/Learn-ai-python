# Simple Polymorphism
# class Dog:
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def speak(self):
#         return "Meow!"

# def animal_sound(animal):
#     print(animal.speak())

# # Both Dog and Cat have the same method 'speak', but with different behavior
# dog = Dog()
# cat = Cat()

# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!

# Polymorphism with inheritance

# class Animal:
#     def speak(self):
#         return "Some sound"

# class Cow(Animal):
#     def speak(self):
#         return "Moo"

# class Sheep(Animal):
#     def speak(self):
#         return "Baa"

# animals = [Cow(), Sheep(), Animal()]

# for animal in animals:
#     print(animal.speak())

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v3)  # Output: (4, 6)
