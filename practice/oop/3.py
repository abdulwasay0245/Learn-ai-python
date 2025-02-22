# Problem : Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size

class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
    def fullname(self):
            return f"{self.brand} {self.model}"

myCar = Car("Toyota", "Camry")
# print(myCar.brand)
# print(myCar.model)

print(myCar.fullname())

class ElectricCar(Car):
     def __init__(self, userbrand, usermodel, battery_size):
          super().__init__(userbrand, usermodel)
          self.battery_size = int(battery_size)

myElectricCar = ElectricCar("Tesla", "Model S", 100)

print(myElectricCar.brand)

print(myElectricCar.model)

print(myElectricCar.fullname())

print(myElectricCar.battery_size)