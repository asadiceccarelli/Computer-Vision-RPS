# Computer Vision Rock Paper Scissors

> Creating a Rock Paper Scissors game using Python and Teachable Machine.

## Milestone 1 - Creating the model

- Each class of rock, paper, scissors and nothing has been trained using Teachable Machine by taking around 300 photos of each class. The more photos used to trained with, the more accurate the model will be.

- The model keras_model.hs and the text files containing the labels, labels.txt, was downloaded from Teachable Machine.

> Insert image of Teachable Machine here.

## Milestone 2

- A virtual environment was created from the terminal with the packages opencv-python, tensorflow and ipykernal install via conda.
    - A virtual environment is used so that we have an isolated environment with only the libraries that we need for this project installed.
    - It also allows someone else who needs to use the code to know exactly what packages they need to run it on their machine.

- The following code was copied from the AiCore Portal, to make use of the model downloaded from Teachable Machine.

- Copied code below:

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

- The above code is a little challenging to understand with my current level of knowledge, however the main key points are to understand that the variable predictions contains the output of the model, and each element in the output corresponds to the probability of the input image representing a particular class.


## Milestone 3

- The program for a manual game of Rock-Paper-Scissors was created using a function to get the user input from the terminal, and to randomly select a choice for the computer.

```python
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

```

## Milestone 4


## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?