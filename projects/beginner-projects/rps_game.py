import random

# rock paper scissor game made by Abdul Wasay PIAIC batch 66  no:250340

def game():
   
        user_input = input("What your choice : r for rock, p for paper ,  s for scissor:\n")
        comp_choice =  random.choice(["r", "p", "s"])
        

        if  user_input not in ("r", "s", "p"):
             print("Please Enter the right value")

        elif user_input == comp_choice :
              print("its a tie")
        
        elif win(user_input, comp_choice):
              print("you won")
        
        else: 
         print("you lost")
        print(f"Your choice is {user_input} and computer's choice is {comp_choice}")

def win(user, computer):
        if(user == 'r'  and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
          return True

        

game()