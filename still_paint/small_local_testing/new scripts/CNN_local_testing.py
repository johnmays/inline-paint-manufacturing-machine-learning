# Some parts of this code are taken from SentDex's tutorial on importing image files for use in tf: https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/

import tensorflow as tf
from tensorflow import keras
import os
import matplotlib.pyplot as plt
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# For the HPC:
# data_directory = '/home/jkm100/augmented_dataset_1'
data_directory = '/Users/johnmays/Documents/Wirth Lab/still_data/Post-Hinc_small_dasets/Post-Hinc_64_64'
dispersion_times = ['01', '03', '08', '15']  # these are the categories
os.chdir(data_directory)
os.getcwd()

train_batches = keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=data_directory, target_size=(64,64), classes=dispersion_times, batch_size=64)


# fully connected network for 2D images:
fc_network = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(units=64, activation=tf.nn.relu),
    keras.layers.Dense(units=64, activation=tf.nn.relu),
    keras.layers.Dense(units=4, activation=tf.nn.softmax)
])


# conv network for 2Dx3 images:
conv_network = keras.Sequential([
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2),
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=4, activation='softmax')
])

# conv_network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  # metrics=['accuracy']

# conv_network.fit(x=train_batches, epochs=20, verbose=2)

fc_network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  # metrics=['accuracy']

fc_network.fit(x=train_batches, epochs=20, verbose=2)
