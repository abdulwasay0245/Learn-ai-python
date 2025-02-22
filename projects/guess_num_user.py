import random
def guessing_game(x):
    low_num = 1
    high_num = x
    user_answer = ""
    while user_answer != "c" and high_num!=low_num:
        if low_num != high_num:
           comp_guess =  random.randint(low_num, high_num)
        else:
            comp_guess = low_num 
        user_answer = input(f"Is {comp_guess} high(H) , low(L), or correct(C):" ).lower()
        if user_answer == "h":
           high_num = comp_guess - 1
        elif user_answer == "l":
            low_num = comp_guess + 1
    print(f"yayyyyy {comp_guess}")

guessing_game(10)

