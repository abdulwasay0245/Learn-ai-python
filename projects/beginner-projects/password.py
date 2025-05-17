import random

print("Generate a Secure password")

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&0123456789'

amount = int(input("ENTER THE AMOUNT OF PASSWORD YOU WANT:  "))
lenght=  int(input("ENTER THE LENGHT OF YOUR PASSWORD:  "))


print('\nHERE ARE YOUR PASSWORDS: ')

for passkey in range(amount):
    password = ''
    for c in range(lenght):
        password += random.choice(characters)
    print(password)

