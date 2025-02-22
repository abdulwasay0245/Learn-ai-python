# Problem : Add a static method to the Car class that returns a general description of a car

# Problem : Modify the Car class to encapsulate the brand attribute . making it private , and provide a getter method  for it

class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel
        Car.total_car += 1
    
    def getBrand(self):
        return self.__brand + "hi"
    def fullname(self):
            return f"{self.__brand} {self.model}"
    @staticmethod
    def general_description():
         return "this car looks good"
print(Car.general_description())
myCar = Car("Toyota", "Camry")
# print(myCar.general_description()) 


# print(myCar.brand)
# print(myCar.model)


# print(myCar.fullname())

class ElectricCar(Car):
     def __init__(self, userbrand, usermodel, battery_size):
          super().__init__(userbrand, usermodel)
          self.battery_size = int(battery_size)

myElectricCar = ElectricCar("Tesla", "Model S", 100)

# print(myElectricCar.brand)

# print(myElectricCar.model)

# print(myElectricCar.fullname())

# print(myElectricCar.battery_size)
# print(myElectricCar.getBrand())

# print(Car.total_car)