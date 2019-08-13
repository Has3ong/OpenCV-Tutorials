import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

model = load_model('myModel.h5')

dog_file = __BASE_DIR__ + 'DATASET'
dog_img = image.load_img(dog_file, target_size=(150, 150))

dog_img = image.img_to_array(dog_img)

dog_img = np.expand_dims(dog_img, axis=0)
dog_img = dog_img/255

prediction_prob = model.predict(dog_img)

print(prediction_prob)