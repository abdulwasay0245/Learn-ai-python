<<<<<<< HEAD
import time
import random

time.sleep(1)
print("Welcome To Business Generator Name")
time.sleep(1.5)
press = str(input("Enter start To Generate name: "))

time.sleep(2)
if(press == "start".lower()):

   busniessman_name = ["Wasay ", "Fahad ", "Hamzah "]
   random_busniessman_name = random.choice(busniessman_name)
#  user_input = str(input("Enter your name : "))

   busniess_type = ["Shipping ", "Car Booking ", "Tarvel Agency "]
   random_busniesstype = random.choice(busniess_type)

   busniess_name_end = ["limited", "Organization", "Co-operation"]
   random_busniess_name_end = random.choice(busniess_name_end)

   print("Generating Your Business Name")
   time.sleep(1.5)
   result = random_busniessman_name + random_busniesstype + random_busniess_name_end
   print(result)
   time.sleep(0.1)
   print("Sucessfully Generated your Business Name")

else:
   print("Please Enter start to Generate")


=======
import time
import random

time.sleep(1)
print("Welcome To Business Generator Name")
time.sleep(1.5)
press = str(input("Enter start To Generate name: "))

time.sleep(2)
if(press == "start".lower()):

   busniessman_name = ["Wasay ", "Fahad ", "Hamzah "]
   random_busniessman_name = random.choice(busniessman_name)
#  user_input = str(input("Enter your name : "))

   busniess_type = ["Shipping ", "Car Booking ", "Tarvel Agency "]
   random_busniesstype = random.choice(busniess_type)

   busniess_name_end = ["limited", "Organization", "Co-operation"]
   random_busniess_name_end = random.choice(busniess_name_end)

   print("Generating Your Business Name")
   time.sleep(1.5)
   result = random_busniessman_name + random_busniesstype + random_busniess_name_end
   print(result)
   time.sleep(0.1)
   print("Sucessfully Generated your Business Name")

else:
   print("Please Enter start to Generate")


>>>>>>> 6c7156682b4a50692bac421b13d9626c1a0c0b8e
