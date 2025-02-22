import random
# import math


# random_num = round(random.random()*10) 

def user_input (x) :
    random_num = random.randint(1, x)
    user_input = 0 
    while random_num != user_input:
          user_input = int(input(f"Enter a number between 1 to {x}:  "  ))
          if random_num > user_input:
               print(f"{user_input} is small than the number")
          elif random_num < user_input:
                if user_input > 10 :
                     print("Your Entered number is greater than the limit")
                else :
                     print(f"{user_input} is greater than the number")
          else :
              print(f"{user_input} Congrats!.. Your guess is correct")


user_input(10)
    
