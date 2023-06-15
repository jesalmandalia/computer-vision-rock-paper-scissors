import random
import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissors:
    '''
    This class is used to play a game of Rock, Paper, Scissors against the computer.
    '''
    
    def __init__(self, computer_player, user_player):
        '''
        Initialise the game.
                
        Args:
            computer (ComputerPlayer): The computer's player object.
            user (UserPlayer): The user's player object. 
        '''
        self.computer = computer_player
        self.user = user_player
            
    def get_winner(self, computer_choice, user_prediction):
        '''
        Compare the computer's choice and the user's choice to determine the winner of the round.
                
        Args:
            computer_choice (str): Computer's choice
            user_prediction (str): User's predicted choice

        Returns:
            str: Result of the round
        '''
        
        if user_prediction == 'Nothing':
            return "Your choice was not recognised. Please try again!"
        elif user_prediction == computer_choice:
            return "It's a tie!"
        elif (user_prediction == 'Rock' and computer_choice == 'Scissors') or \
                (user_prediction == 'Paper' and computer_choice == 'Rock') or \
                (user_prediction == 'Scissors' and computer_choice == 'Paper'):
            return "You won!"
        else:
            return "You lost"

    def play(self):
        '''
        Play a game of Rock, Paper, Scissors against the computer.
        The game is played until either the computer or the user reaches the specified number of wins.
        '''
        
        computer_wins = 0 
        user_wins = 0
        while True:
            computer_choice = self.computer.get_computer_choice()
            user_prediction = self.user.get_prediction()
            result = self.get_winner(computer_choice, user_prediction)

            if result == "You won!":
                user_wins += 1
            elif result == "You lost":
                computer_wins += 1

            print("You chose: " + user_prediction)
            print("The computer chose: " + computer_choice)
            print("This round: " + result)
            print("The score is: " + str(user_wins) + " to " + str(computer_wins))
            
            if user_wins == 3 or computer_wins == 3:
                break

        if user_wins == 3:
            print("Congratulations! You won the game!")
        else:
            print("Game over. You lost the game.")


class ComputerPlayer:
    '''
    This class is used to generate the computer's choice.
    '''
    
    def get_computer_choice(self):
        '''
        Randomly generate the computer's choice of Rock, Paper, or Scissors.
        
        Returns:
            str: Computer's choice
        '''
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        return computer_choice

class UserPlayer:
    '''
    This class predicts the user's choice Rock, Paper, Scissors or Nothing using a pre-trained model.
    '''
    
    def get_prediction(self):
        '''
        The webcam feed is processed using the model to predict the user's choice.
        The prediction is based on the maximum value in the prediction array.
        The index of the maximum value is used to determine the user's choice given the order in label.txt.
        
        Returns:
            str: User's predicted choice
        '''
        
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        print("Get ready to play Rock, Paper, Scissors!")
        print("Rock, Paper, Scissors!")
        print("3, 2, 1, Go!")

        countdown_duration = 3  
        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1  
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Either press q to close the window else it will close after the countdown duration
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q') or elapsed_time >= countdown_duration:
                break

        cap.release()
        cv2.destroyAllWindows()

        choice = np.argmax(prediction)
        
        choice_list = ['Rock', 'Paper', 'Scissors', 'Nothing'] 
        user_prediction = str(choice_list[choice]) 
        return user_prediction


# Start the game
computer_player = ComputerPlayer()
user_player = UserPlayer()
game = RockPaperScissors(computer_player, user_player)
game.play()
