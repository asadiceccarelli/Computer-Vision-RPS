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
        print('You won!')
    elif computer_choice == 'R' and user_choice == 'S':
        print('Sorry, you lose.')
    elif computer_choice == 'P' and user_choice == 'R':
        print('Sorry, you lose.')
    elif computer_choice == 'P' and user_choice == 'S':
        print('You won!')
    elif computer_choice == 'S' and user_choice == 'R':
        print('You won!')
    elif computer_choice == 'S' and user_choice == 'P':
        print('Sorry, you lose.')
    elif computer_choice == user_choice:
        print('Draw.')
    else:
        print('Sorry, you did not enter a valid choice.')


def play():
    computer_choice = get_computer_choice(options)
    user_choice = get_user_choice()
    return get_winner(computer_choice, user_choice)

play()
