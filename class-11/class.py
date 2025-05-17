class House:
    address: str
    name: str = "Fahad House"
    street: int

    def say_hi(self):
        print('Hello, my name is', self.name)
    def __init__(self, house_no, name , streets):
        self.address = house_no
        self.street = streets
        self.name = name

house = House("Pak Kausar Town", "wasay house", 35)
print(house.address)
print(house.name)
print(house.street)
house.say_hi()