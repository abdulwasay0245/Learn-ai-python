class Person:
    name: str
    __sceret: int
    _age: int
    

    def __init__(self, name, secret, age):
        self.name = name
        self.__sceret = secret
        self._age = age


    def get_age(self):
        return self.__sceret
    
    def set_secret(self, new_secret):
        if self.__sceret > 10:
            self.__sceret = new_secret
            print(new_secret)
        else:
            print(self.__sceret)

class Student(Person):
    
    def introduce(self):
        print(f"The Student name is {self.name} and age is {self._age}")


person_1 = Person(name="Fahad", secret=12, age= 17)
# print(person_1.get_age())
person_1.set_secret(new_secret=13)
# person_2 = Person(name="Wasay", secret="fdf", age=200 )



# print(f"{person_1.name} {person_2.name}")

# std_1 = Student(name="Fahad", secret="hacker", age= 13)
# print(std_1.name, std_1._age)