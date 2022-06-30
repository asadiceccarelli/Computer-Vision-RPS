import random

options = ['Rock', 'Paper', 'Scissors']
computer_wins = 0
user_wins = 0


def get_computer_choice(options):
    computer_choice = random.choice(options)
    return computer_choice


def get_user_choice():
    user_choice = input('Please enter either Rock, Paper, or Scissors: ')
    return user_choice


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
    


def play():
    computer_choice = get_computer_choice(options)
    user_choice = get_user_choice()
    return get_winner(computer_choice, user_choice)


