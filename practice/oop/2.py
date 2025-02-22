# Problem : Add a method to the car class that displays the full name of the car(brand and model)
class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
    def fullname(self):
            return f"{self.brand} {self.model}"

myCar = Car("Toyota", "Camry")
print(myCar.brand)
print(myCar.model)

print(myCar.fullname())
