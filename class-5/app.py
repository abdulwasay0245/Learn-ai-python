wasay = 18
fahad = 10

if wasay != fahad:
    print("congrats")

num_1 = 4
num_2 = 4

print(num_1 != num_2) # false
print(num_1 == num_2) # true
print(num_1 > num_2) # false
print(num_1 < num_2) # false
print(num_1 >= num_2) # true
print(num_1 <= num_2) # true
print(2 - num_1 == num_2 - 2) # false
print(2 - num_1 <= num_2 - 2) # true

compare = num_1 and num_2
print(f'The value is {compare}')

name_1 = "fahad"
name_2 = "wasay"


print(name_1 == name_2) # false
print(name_1 != name_2) # true
print(name_1 < name_2) # true
print(name_1 > name_2) # false
print(name_1 <= name_2) # true
print(name_1 >= name_2) # false

# String
print("Sring Method")
country_1 = "uk zindabad"
country_2 = "uk zindabad"

print(country_1.lower() == country_2.lower())
print(country_1.upper() == country_2.upper())
print(country_1.title() == country_1.title())
print(country_1.capitalize() == country_2.capitalize())
print(country_1.find("zindabad"))

if (country_1.find("uk") == 0) :
  print("Sucess")
else: 
   print("Reject")




print(False and True or False)
print(not True and False or True)
print(not True or False and True)
print(not False and True or False)
print(not False or True and False)
