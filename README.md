
Rock, paper, scissors is a classic game played between two people to settle disputes or simply for fun. The players simultaneously display one of three hand gestures: rock, paper, or scissors. Rock beats scissors by crushing it, scissors beat paper by cutting it, and paper beats rock by covering it.

In this implementation of the game, I introduce an interactive twist where the user can play against the computer by making hand gestures in front of their camera.


- [Creating the Computer Vision System](#creating-the-computer-vision-system)
- [Milestone 4, Creating a Rock Paper and Scissors Game](#milestone-4-creating-a-rock-paper-and-scissors-game)
	- [get\_computer\_choice()](#get_computer_choice)
	- [get\_user\_choice()](#get_user_choice)
	- [get\_winner(computer\_choice, user\_choice)](#get_winnercomputer_choice-user_choice)
	- [play()](#play)


# Creating the Computer Vision System

To create the computer vision model for this game, I leveraged the power of [Teachable-Machine](https://teachablemachine.withgoogle.com). The following steps were taken to develop the model:

1) Training Data: I uploaded images representing four classes: rock, paper, scissors, and nothing. These images showcase different hand gestures for each option.
2) Model Creation: Using the Teachable Machine interface, I trained a model based on the provided images. This model is used to recognise and classify the hand gestures accurately.
3) Model Output: After the training process, the model was downloaded from the "Tensorflow" tab. The resulting model is named keras_model.h5 and the corresponding text file containing the labels is named labels.txt.


# Milestone 4, Creating a Rock Paper and Scissors Game

The `manual_rps.py` file simulates a rock, paper and scissors game by using typed input from the user. Four functions were used to create the game simulation. 

## get_computer_choice()
The `get_computer_choice()` function randomly selects between "rock", "paper" and "scissors" and returns the computer's choice as a string. It uses the `random.choice()` function to pick a random element from the given list of choices.

## get_user_choice()
The `get_user_choice()` function asks the user to input their choice. The user's choice is then converted into lowercase for consistency. The user's choice is returned as a string.

## get_winner(computer_choice, user_choice)
The `get_winner(computer_choice, user_choice)` function takes two arguments, `get_computer_choice()` and `get_user_choice()`. The computer and user choice is compared and the winner following the game logic is decided. If the user wins "You won!" is printed and if the user loses "You lost" is printed. When the user and the computer have made the same choice "It is a tie!" is printed. If none of these conditions is met then there is an error with the user input and a message saying "Invalid input!" is printed. 

## play()

The `play()` function simulates the game by calling the necessary functions. It gets the computer's choice, prompts the user for their choice, and determines the winner based on the choices. The result is then printed.
