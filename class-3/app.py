import random

# name = "fahad"
# if name == "fahad":
#     print("Pass")
# else:
#     print("Reject")

# name_2 = "wasay"
# while name_2 != "wasay": 
#     print("Reject")

# userinput = input("Enter Your Name")
# print(userinput)

# if userinput == "fahad":
#     print(f"You Select Name {userinput}")
# elif userinput == "wasay":
#     print(f"You Select Name {userinput}")

def number(num): 
    num_1 = random.randint(1, num)
    num_2 = 0

    while num_1 != num_2:
        num_2 =  int(input('Please Select a Number between 1 to 10: '))

        if num_2 > 10:
            print("Please Enter Number Less Than 10")
        else:    
            if num_1 == num_2:
              print(f"Congrats You Select Correct Number: {num_1}")
            elif num_1 != num_2:
              print(f"Sorry you choose wrong number: {num_2}")
number(10)



# print(f"HI Fahad\nyou got a free coupon")

# print(f"""
#      Hi I'm {number}
#      i'm from karachi
#         """)