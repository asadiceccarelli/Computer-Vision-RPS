import cv2
from keras.models import load_model
import numpy as np
import time
import random

class RPS:
    def __init__(self, wins_needed=3):
        self.wins_needed = wins_needed
        self.options = ['Rock', 'Paper', 'Scissors']
        self.computer_wins = 0
        self.user_wins = 0
    

    def get_computer_choice(self):
        computer_choice = random.choice(self.options)
        return computer_choice


    def timer(self):
        counter = 3
        while counter > 0:
            print(f'Show your hand in {counter}...')
            time.sleep(1)
            counter -= 1
        print('Show your hand!')
    

    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            # Prediction contains the output of the model
            # Each element corresponds to probability the input image represents a particular class
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            self.timer()
            return prediction
                    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()


    def get_winner(self, computer_choice, user_choice):
        
        if computer_choice == 'Rock' and user_choice == 'Paper':
            print('You won! Paper beats Rock.')
            self.user_wins += 1
        elif computer_choice == 'Rock' and user_choice == 'Scissors':
            print('You lose. Rock beats Scissors.')
            self.computer_wins += 1
        elif computer_choice == 'Paper' and user_choice == 'Rock':
            print('You lose. Paper beats Rock.')
            self.computer_wins += 1
        elif computer_choice == 'Paper' and user_choice == 'Scissors':
            print('You won! Scissors beats Paper.')
            self.user_wins += 1
        elif computer_choice == 'Scissors' and user_choice == 'Rock':
            print('You won! Rock beats Scissors.')
            self.user_wins += 1
        elif computer_choice == 'Scissors' and user_choice == 'Paper':
            print('You lose. Scissors beats Paper.')
            self.computer_wins += 1
        elif computer_choice == user_choice:
            print('Draw.')
        else:
            print('Sorry, you did not enter a valid choice.')

    def play_game(self):
        while self.computer_wins < self.wins_needed and self.user_wins < self.wins_needed:
            prediction = self.get_prediction()
            computer_choice = self.get_computer_choice()
            choice_probability = {'Rock': prediction[0,0], 'Paper': prediction[0,1], 'Scissors': prediction[0,2]}
            user_prediction = max(choice_probability, key=choice_probability.get)

            print(f'\nComputer went with {computer_choice}.')
            print(f'You went with {user_prediction}.')
            self.get_winner(computer_choice, user_prediction)
            print(f'\nSCORE: You: {game.user_wins} vs. {game.computer_wins} Computer\n')
            time.sleep(1)
            if self.computer_wins == self.wins_needed:
                print(f'Computer has reach {self.wins_needed} wins. You have lost the game.\n')
                return
            elif self.user_wins == self.wins_needed:
                print(f'You have reach {self.wins_needed} wins. Congratulations, you have won the game!\n')
                return

if __name__ == '__main__':
    game = RPS(wins_needed = 3)
    game.play_game()
