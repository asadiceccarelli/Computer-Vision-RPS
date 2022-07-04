# Computer Vision Rock Paper Scissors

> Creating a Rock Paper Scissors game using Python and Teachable Machine.

## Milestone 1 - Creating the model

- Each class of rock, paper, scissors and nothing has been trained using Teachable Machine by taking around 300 photos of each class. The more photos used to trained with, the more accurate the model will be.

- The model keras_model.hs and the text files containing the labels, labels.txt, was downloaded from Teachable Machine.

![Teachable Machine](ReadMe_Images/Teachable_Machine.png 'Teachable Machine')

> Creating the Teachable Machine model.

## Milestone 2

- A virtual environment was created from the terminal with the packages opencv-python, tensorflow and ipykernal install via conda.
    - A virtual environment is used so that we have an isolated environment with only the libraries that we need for this project installed.
    - It also allows someone else who needs to use the code to know exactly what packages they need to run it on their machine.

- The following code was copied from the AiCore Portal, to make use of the model downloaded from Teachable Machine.

```python
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```

> The copied code.

- The above code is a little challenging to understand but the main key points are to understand that the variable predictions contains the output of the model, and each element in the output corresponds to the probability of the input image representing a particular class.


## Milestone 3

- The program for a manual game of Rock-Paper-Scissors was created using a function to get the user input from the terminal, and to randomly select a choice for the computer.

```python
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

```

> This shows the code of the manual_rps.py program.

## Milestone 4

- A new file named camera_rps.py was created for the code of the final Rock-Paper-Scissors game using the camera.
    - Here copied code for the camera input was turned into a function get_prediction and imported into camera_rps.py.
    - The function get_winner was also copied from the manual_rps.py game and inserted into camera_rps.py.

- A timer function was also added to the get_prediction function to count down from 3.

- A feature was added where the first person (user or computer) to reach 3 wins would win the game was added.

```python
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
```

> The main while loop in camera_rps.py

## Conclusions

- Although the initial code on using the computer vision software was difficult to decipher, once a clear plan was established on how to go about the rest of the program it was not too challenging.

- This was the first project where I have stuck to using git to work on different branches, before commiting them and pushing them to GitHub all via the terminal. It was confusing at first and I had a couple of problems along the way (especially with .DS_Store files), but eventually I got my head around it. I will continue to use git throghout future project as it is far neater than creating various 'x_copy_test_version2' files along the way to do various tests, and is an important part of any collaborative work in software.

## Further Work

- Since completing this project I have created another file oop_rps.py which works in the same way as camera_rps.py, but uses Object Orientated Programming, creating a class RPS. This is a little cleaner than using multiple functions as was previously done.

### Future additions
- Recreate model on Teachable Machine with more photos in order to improve accuracy
- Print countdown on web display
- Include a message such as 'press c to continue'