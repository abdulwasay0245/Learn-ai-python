<<<<<<< HEAD
import time
import random

# 1
def greet(name):
    
    print(f'Hello, {name}!')

greet("Wasay")

time.sleep(5)
# 2
def greet2(name = 'Fahad'):
    
    print(f'Hello, {name}!')

greet2()

# 3
def sum(num1 :int , num2 : int):
    print(num1 + num2)

sum(10 ,12)

# 4
helloworld = lambda :print('wasay')
helloworld()

# Timepass
busines_type = ['shipping' , 'booking', 'travel_agency', ]
random_name = random.choice(busines_type)
print(random_name)
shipping_name = ['fahadshipping', 'wasayshipping', 'hamzahshipping' ]
booking_name = ['booking.com', 'ticketwala', 'airbnb']

if(random_name == 'shipping'):
   random_ship = random.choice(shipping_name)
   print(f'your shipping business name is {random_ship}')
elif(random_name == 'booking'):
   random_book = random.choice(booking_name)
   print(f'your shipping business name is {random_book}')
=======
import time
import random

# 1
def greet(name):
    
    print(f'Hello, {name}!')

greet("Wasay")

time.sleep(5)
# 2
def greet2(name = 'Fahad'):
    
    print(f'Hello, {name}!')

greet2()

# 3
def sum(num1 :int , num2 : int):
    print(num1 + num2)

sum(10 ,12)

# 4
helloworld = lambda :print('wasay')
helloworld()

# Timepass
busines_type = ['shipping' , 'booking', 'travel_agency', ]
random_name = random.choice(busines_type)
print(random_name)
shipping_name = ['fahadshipping', 'wasayshipping', 'hamzahshipping' ]
booking_name = ['booking.com', 'ticketwala', 'airbnb']

if(random_name == 'shipping'):
   random_ship = random.choice(shipping_name)
   print(f'your shipping business name is {random_ship}')
elif(random_name == 'booking'):
   random_book = random.choice(booking_name)
   print(f'your shipping business name is {random_book}')
>>>>>>> 6c7156682b4a50692bac421b13d9626c1a0c0b8e
