import random
def guess_number():

    input_number = int(input("Enter Number Between 0 to 50: "))

    random_number = random.randint(0, 50)

    
    while input_number != random_number:
        while(input_number>=51):
            print("Your Number is Greator Than 50")
            break
        else:
            print(f"Random Number is => {random_number}")

            if(input_number < random_number):
               print("your guess is too low")
            elif(input_number > random_number):
               print("your guess is too high")

            input_number = int(input("Enter a new Guess Number: "))
            random_number = random.randint(0, 50)
    else:
        print(f"Yeah you Win computer choose {random_number}")

guess_number()