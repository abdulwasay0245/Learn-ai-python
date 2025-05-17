# ass 1
class Programmer:
    name: str 
    age: int 
    experience: int

    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience= experience
        
programmer1 = Programmer("wasay", 19, 3955)
programmer2 = Programmer("fahad", 19, 398)
programmer3 = Programmer("abdul", 134, 439)
programmer4 = Programmer("ali", 195, 559)


arr = [programmer1,programmer2,programmer3,programmer4]

for name in arr:
    print(name.name, name.age, name.experience)

# ass 2
class Calculator:

    def square(self, num1):
        result = self.number = num1 ** 2
        return result
    
    def add(self, num1):
        result = self.number = num1 + num1
        return result
        

find = Calculator()
show = find.square(5)
print(show)

addition = find.add(3)


print(addition)



# assignment 3

class A:
    a:str =  "b" 


obj = A()

obj.a= "o"
obj2 = A()

print(obj.a)
print(obj2.a)

# assignment 4

class Calculators:

    @staticmethod
    def square(num1):
        result = num1 ** 2
        return result
    @staticmethod
    def add(num1):
        result =  num1 + num1
        return result
        

static = Calculators()

shows = static.square(3)
print(shows)

adds = static.add(3)
print(adds)

# assignment 5
user 
class Train:
