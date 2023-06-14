import random

def get_computer_choice():
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    return computer_choice

def get_user_choice():
    user_choice = input("Please enter your choice of Rock, Paper, Scissors: ")
    #user_choice = user_choice.lower()
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    elif computer_choice == 'Rock' and user_choice == 'Paper':     
        print("You won!")
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        print("You lost")
    elif computer_choice == 'Paper' and user_choice == 'Rock':     
        print("You lost")
    elif computer_choice == 'Paper' and user_choice == 'Scissors':
        print("You won!")
    elif computer_choice == 'Scissors' and user_choice == 'Rock':
        print("You won!")
    elif computer_choice == 'Scissors' and user_choice == 'Paper':
        print("You lost")
    #else:   
    #    print("Invalid input!") 
        
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print("The computer chose: " + computer_choice)
    get_winner(computer_choice, user_choice)

play()