class Person:
    name: str
    __sceret: str
    _age: int
    

    def __init__(self, name, secret, age):
        self.name = name
        self.__sceret = secret
        self._age = age


class Student(Person):
    
    def introduce(self):
        print(f"The Student name is {self.name} and age is {self._age}")


person_1 = Person(name="Fahad", secret="Non", age= 17)
person_2 = Person(name="Wasay", secret="fdf", age=200 )

print(f"{person_1.name} {person_2.name}")

std_1 = Student(name="Fahad", secret="hacker", age= 13)
print(std_1.name, std_1._age)