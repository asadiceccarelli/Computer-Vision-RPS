import cv2
from keras.models import load_model
import numpy as np
import time
import random
from camera_input import get_prediction

computer_wins = 0
user_wins = 0


def get_computer_choice():
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    return computer_choice


def get_winner(computer_choice, user_choice):
    global computer_wins, user_wins
    if computer_choice == 'Rock' and user_choice == 'Paper':
        print('You won! Paper beats Rock.')
        user_wins += 1
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        print('You lose. Rock beats Scissors.')
        computer_wins += 1
    elif computer_choice == 'Paper' and user_choice == 'Rock':
        print('You lose. Paper beats Rock')
        computer_wins += 1
    elif computer_choice == 'Paper' and user_choice == 'Scissors':
        print('You won! Scissors beats Paper.')
        user_wins += 1
    elif computer_choice == 'Scissors' and user_choice == 'Rock':
        print('You won! Rock beats Scissors.')
        user_wins += 1
    elif computer_choice == 'Scissors' and user_choice == 'Paper':
        print('You lose. Scissors beats Paper.')
        computer_wins += 1
    elif computer_choice == user_choice:
        print('Draw.')
    else:
        print('Sorry, you did not enter a valid choice.')


while computer_wins < 3 and user_wins < 3: 
    prediction = get_prediction()
    computer_choice = get_computer_choice()
    choice_probability = {'Rock': prediction[0,0], 'Paper': prediction[0,1], 'Scissors': prediction[0,2]}
    user_prediction = max(choice_probability, key=choice_probability.get)

    print(f'\nComputer went with {computer_choice}.')
    print(f'You went with {user_prediction}.')
    game_result = get_winner(computer_choice, user_prediction)
    print(f'\nSCORE: You: {user_wins} vs. {computer_wins} Computer\n')
    time.sleep(1)
    if computer_wins == 3:
        print(f'Computer has reach 3 wins. You have lost the game.\n')
        break
    elif user_wins == 3:
        print(f'You have reach 3 wins. Congratulations, you have won the game!\n')
        break

