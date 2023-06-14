import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    # Randomly choose between Rock, Paper, and Scissors
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    return computer_choice

def get_user_choice():
    # Load the model and start the webcam feed for capturing images to predict the user's choice    
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Print instructions for the user
    print("Get ready to play Rock, Paper, Scissors!")
    print("Rock, Paper, Scissors!")
    print("3, 2, 1, Go!")

    countdown_duration = 3  # 3-second countdown
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = countdown_duration - elapsed_time

        # Read frame from webcam and process it for prediction
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalise the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Either press q to close the window else it will close after the countdown duration
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q') or elapsed_time >= countdown_duration:
            break

    cap.release()
    cv2.destroyAllWindows()
    
    # Get the user's choice based on the highest predicted value
    choice = np.argmax(prediction)
    
    # Map the predicted value to the corresponding choice and return it
    # The file labels.txt determines the order of the list
    choice_list = ['Rock', 'Paper', 'Scissors', 'Nothing'] 
    user_choice = str(choice_list[choice]) 
    return user_choice

def get_winner(computer_choice, user_choice):
    valid_choices = ["Rock", "Paper", "Scissors"]

    # Check if user's choice is valid
    if user_choice not in valid_choices:
        return "Invalid choice! Please choose Rock, Paper, or Scissors."
    # Check for tie
    elif user_choice == computer_choice:
        return "It's a tie!"
    # Check for user win conditions
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Paper' and computer_choice == 'Rock') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You won!"
    else:
        return "You lost"

def play():
    # Play a 3-round game of Rock Paper Scissors    
    computer_score = 0 # Initialise scores
    user_score = 0
    while True:
        # Get computer and user choices for this round and determine the winner 
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        result = get_winner(computer_choice, user_choice)

        # Print user's choice, computer's choice, and the result of the round
        print("You chose: " + user_choice)
        print("The computer chose: " + computer_choice)
        print("This round: " + result)

        # Update scores based on the result
        if result == "You won!":
            user_score += 1
        elif result == "You lost!":
            computer_score += 1

        # Print the current score
        print("The score is: " + str(user_score) + " to " + str(computer_score))

        # Check if any player has reached a score of 3 and end the game
        if user_score == 3 or computer_score == 3:
            break

    # Print the final result of the game
    if user_score == 3:
        print("Congratulations! You won the game!")
    else:
        print("Game over. You lost the game.")

# Start the game
play()
