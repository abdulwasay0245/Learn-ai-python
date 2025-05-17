class Animal:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        sound = "Animal Sound"
        return sound
    # Iski Pefernce low kiov kay niche 

class Cat(Animal):

    cat_food: str

    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.cat_food = food
        
    # def meow(self):
    #     voice = "Meow"
    #     return voice

    # def make_sound(self):
    #     return super().make_sound()
    #  humay niche cat kay variable may iski value deni pare ge

    def make_sound(self):
        vioce = "Meow"
        return vioce

class Dog(Animal):
    def bark(self):
        voice = "Bark"
        return voice

#  For Cat
cat = Cat("Tom", 5, "Cat Food")
cat_2 = Cat("Kitty", 3, "Cat Food")

print(cat.name, cat.age, cat.make_sound(), cat.cat_food )
# print(cat_2.name, cat_2.age, cat.make_sound(), cat.cat_food )


# #  For Dog
# dog = Dog("Spike", 8)
# dog_2 = Dog("Sefart", 4)

# print(dog.name, dog.age, dog.bark())
# print(dog_2.name, dog_2.age, dog_2.bark())