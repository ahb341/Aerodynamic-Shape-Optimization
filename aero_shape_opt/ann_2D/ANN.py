import random
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
print(tf.__version__)

def run_ANN(af):
   # ANN Model
   # Input - a column vector containing the x and y coordinates

   input = np.array([af.interp_x,af.interp_y]).flatten('F')

   model = tf.keras.Sequential(
   [
      tf.keras.layers.Input(shape=(28*28,)),
      tf.keras.layers.Dense(200, activation='relu'),
      tf.keras.layers.Dropout(0.25),
      tf.keras.layers.Dense(100, activation='relu'),
      tf.keras.layers.Dropout(0.25),
      tf.keras.layers.Dense(60, activation='relu'),
      tf.keras.layers.Dropout(0.25),
      tf.keras.layers.Dense(10, activation='softmax')
   ])

   model.compile(optimizer='adam',
               loss='categorical_crossentropy',
               metrics=['accuracy'])

   # print model layers
   model.summary()            
