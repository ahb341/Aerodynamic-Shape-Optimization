import random
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
print(tf.__version__)

# CNN Model
def generateModel():
   model = keras.Sequential([
      layers.Input(shape=(64,64,1)),
      # Feature Learning
      # First convolutional layer
      layers.Conv2D(32,3,padding='valid',activation='relu'),
      layers.MaxPooling2D(pool_size=(2,2)),

      # Second convolutional layer
      layers.Conv2D(64,3,activation='relu'),
      layers.MaxPooling2D(pool_size=(2,2)),

      # Third convolutional layer
      # layers.Conv2D(128,3,activation='relu'),
      # layers.MaxPooling2D(pool_size=(2,2)),

      # Fully connected regression
      layers.Flatten(),
      layers.Dense(1024,activation='relu'),
      layers.Dense(64,activation='relu'),
      layers.Dense(3) # 3 outputs: cl, cd, cm
   ])
   return model

model = generateModel()

model.compile(optimizer='adam',
   loss='categorical_crossentropy',
   metrics=['accuracy'])

# print model layers
model.summary()            
