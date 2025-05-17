import random
import time
time.sleep(1)
print("Welcome to the number guessing game!")
time.sleep(1)
print("This game is consist of 5 rounds.")
time.sleep(1)

points = 0
count = 1
for i in range(5, 0, -1):
    print(f"Round {count}")
    user_num = random.randint(1, 100)
    comp_num = random.randint(1, 100)
    print(f"Your number is: {user_num}")
    time.sleep(1)
    user_guess = str(input("Do you think your number is higher or lower than the computer's?: "))
    while user_guess != "higher" and user_guess != "lower":
        print("Invalid input!")
        user_guess = str(input("Do you think your number is higher or lower than the computer's?: "))
    
    if user_guess == "higher" and user_num > comp_num:
        print(f"The computer's number is: {comp_num}")
        print("You win!")
        points += 1
    elif user_guess == "lower" and user_num < comp_num:
        print(f"The computer's number is: {comp_num}")
        print("You win!")
        points += 1
    elif user_guess == "higher" and user_num < comp_num:
        print(f"The computer's number is: {comp_num}")
        print("You lose!")
    elif user_guess == "lower" and user_num > comp_num:
        print(f"The computer's number is: {comp_num}")
        print("You lose!")
    else:
        print("Invalid input!")
    print(f"Your points are: {points}")

    count += 1
    time.sleep(1)


