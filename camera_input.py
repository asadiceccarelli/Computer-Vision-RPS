import cv2
from keras.models import load_model
import numpy as np
import time


def timer():
    counter = 3
    while counter > 0:
        print(f'Show your hand in {counter}...')
        time.sleep(1)
        counter -= 1
    print('Show your hand!')


def get_prediction():
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
        timer()
        return prediction
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


