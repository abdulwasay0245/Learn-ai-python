class Animal:
    names:str
    ages:int

    def __init__(self, names, ages):
        self.name = names
        self.age = ages


class Cat(Animal):
    cat_food: str

    def __init__(self, names, ages, cat_foods):
        super().__init__(names, ages)
        self.cat_foods = cat_foods
        

cat = Cat("Tom", 5, "fish")
print( cat.cat_foods)