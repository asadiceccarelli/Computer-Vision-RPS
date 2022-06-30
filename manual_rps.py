import random

options = ['R', 'P', 'S']


def get_computer_choice(options):
    computer_choice = random.choice(options)
    return computer_choice


def get_user_choice():
    user_choice = input('Please enter either R, P, or S: ')
    return user_choice


def get_winner(computer_choice, user_choice):
    if computer_choice == 'R' and user_choice == 'P':
        return 'You won!'
    elif computer_choice == 'R' and user_choice == 'S':
        return 'Sorry, you lose.'
    elif computer_choice == 'P' and user_choice == 'R':
        return 'Sorry, you lose.'
    elif computer_choice == 'P' and user_choice == 'S':
        return 'You won!'
    elif computer_choice == 'S' and user_choice == 'R':
        return 'You won!'
    elif computer_choice == 'S' and user_choice == 'P':
        return 'Sorry, you lose.'
    elif computer_choice == user_choice:
        return 'Draw.'
    else:
        return 'Sorry, you did not enter a valid choice.'

print('test')