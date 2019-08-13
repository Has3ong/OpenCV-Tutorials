from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense, Conv2D, MaxPooling2D
import warnings
import matplotlib.pyplot as plt
import os

__BASE_DIR__ = os.path.dirname(os.path.realpath(__file__))

# {'CAT': 0, 'DOG': 1}

image_gen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rescale=1/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

image_shape = (150,150,3)

model = Sequential()

model.add(Conv2D(filters=32, kernel_size=(3,3),input_shape=(150,150,3), activation='relu',))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3,3),input_shape=(150,150,3), activation='relu',))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3,3),input_shape=(150,150,3), activation='relu',))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(128))
model.add(Activation('relu'))

model.add(Dropout(0.5))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model.summary()

batch_size = 16

train_image_gen = image_gen.flow_from_directory(
    __BASE_DIR__ + 'DATASET',
    target_size=image_shape[:2],
    batch_size=batch_size,
    class_mode='binary'
)

test_image_gen = image_gen.flow_from_directory(
    __BASE_DIR__ + 'DATASET',
    target_size=image_shape[:2],
    batch_size=batch_size,
    class_mode='binary'
)

warnings.filterwarnings('ignore')

results = model.fit_generator(
    train_image_gen, epochs=100,
    steps_per_epoch=50,
    validation_data=test_image_gen,
    validation_steps=12
)

plt.plot(results.history['acc'])
plt.show()

model.save('myModel.h5')