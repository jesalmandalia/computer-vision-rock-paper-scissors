
Rock, paper, scissors is a classic game played between two people to settle disputes or simply for fun. The players simultaneously display one of three hand gestures: rock, paper, or scissors. Rock beats scissors by crushing it, scissors beat paper by cutting it, and paper beats rock by covering it.

In this implementation of the game, I introduce an interactive twist where the user can play against the computer by making hand gestures in front of their camera.


- [Create the Computer Vision System](#create-the-computer-vision-system)

# Create the Computer Vision System

To create the computer vision model for this game, I leveraged the power of [Teachable-Machine](https://teachablemachine.withgoogle.com). The following steps were taken to develop the model:

1) Training Data: I uploaded images representing four classes: rock, paper, scissors, and nothing. These images showcase different hand gestures for each option.
2) Model Creation: Using the Teachable Machine interface, I trained a model based on the provided images. This model is used to recognise and classify the hand gestures accurately.
3) Model Output: After the training process, the model was  downloaded from the "Tensorflow" tab. The resulting model is named keras_model.h5 and the corresponding text file containing the labels is named labels.txt.



