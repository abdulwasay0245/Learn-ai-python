# This program doubles the input number entered by the user until it is greater than 100

current_number = int(input("Enter a number: "))
if current_number > 100:
    print("Enter a number less than 100")
else:
    print("Result")

def double_it(number):
  
     return number * 2

while current_number < 100:
    current_number = double_it(current_number)
    print(current_number)


