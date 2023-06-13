import random

def get_computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice

def get_user_choice():
    user_choice = input("Please enter your choice: ")
    user_choice = user_choice.lower()
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    elif computer_choice == 'rock' and user_choice == 'paper':     
        print("You won!")
    elif computer_choice == 'rock' and user_choice == 'scissors':
        print("You lost!")
    elif computer_choice == 'paper' and user_choice == 'rock':     
        print("You lost!")
    elif computer_choice == 'paper' and user_choice == 'scissors':
        print("You won!")
    elif computer_choice == 'scissors' and user_choice == 'rock':
        print("You won!")
    elif computer_choice == 'scissors' and user_choice == 'paper':
        print("You lost!")
    else:   
        print("Invalid input!") 
        
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print("The computer chose: " + computer_choice)
    get_winner(computer_choice, user_choice)

play()