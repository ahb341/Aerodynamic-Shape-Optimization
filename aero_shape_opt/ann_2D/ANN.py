import random
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

def generate_ANN(input, output):
   # ANN Model
   # Input - an arbitrary vector to size the input of the ANN

   # input = np.array([af.interp_x,af.interp_y]).flatten('F')

   model = tf.keras.Sequential(
   [
      tf.keras.layers.Input(shape=(len(input),)),
      # tf.keras.layers.Dense(200, activation='relu'),
      # tf.keras.layers.Dropout(0.25),
      # tf.keras.layers.Dense(100, activation='relu'),
      # tf.keras.layers.Dropout(0.25),
      # tf.keras.layers.Dense(60, activation='relu'),
      # tf.keras.layers.Dropout(0.25),

      # tf.keras.layers.Dense(100, activation='relu'),
      # tf.keras.layers.Dropout(0.25),
      # tf.keras.layers.Dense(100),
      # tf.keras.layers.Dense(60),

      tf.keras.layers.Dense(350, activation='relu'),
      tf.keras.layers.Dropout(0.20),
      tf.keras.layers.Dense(300, activation='relu'),
      tf.keras.layers.Dropout(0.20),
      tf.keras.layers.Dense(270, activation='relu'),
      tf.keras.layers.Dropout(0.20),
      tf.keras.layers.Dense(220, activation='relu'),
      tf.keras.layers.Dropout(0.20),
      tf.keras.layers.Dense(160, activation='relu'),
      tf.keras.layers.Dropout(0.20),
      tf.keras.layers.Dense(120, activation='relu'),
      tf.keras.layers.Dropout(0.20),
      tf.keras.layers.Dense(60, activation='relu'),
      tf.keras.layers.Dropout(0.20),
      tf.keras.layers.Dense(10, activation='relu'),
      tf.keras.layers.Dropout(0.20),
      # tf.keras.layers.Dense(25, activation='relu'),
      # tf.keras.layers.Dropout(0.15),
      # tf.keras.layers.Dense(20, activation='relu'),
      # tf.keras.layers.Dropout(0.15),

      tf.keras.layers.Dense(len(output), activation='softmax')
   ])

   model.compile(optimizer=keras.optimizers.Adam(lr=1e-4),#'adam',
               loss='categorical_crossentropy',
               metrics=['accuracy'])

   # model.compile(loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False), # set to true if not using softmax on last layer
   #            optimizer=keras.optimizers.Adam(lr=0.001), # implement Adam algorithm with a learning rate
   #            metrics=['accuracy'])

   # print model layers
   model.summary()

   return model


data = np.load('aero_shape_opt\\datasets\\data_file_ann.npz',allow_pickle=True)
x_train = data['x_train']
x_test = data['x_test']
y_train = data['y_train']
y_test = data['y_test']

model = generate_ANN(x_train[0],y_train[0])

x_train_tens = np.array(x_train) #np.array([np.asarray(i) for i in x_train])
x_test_tens  = np.array(x_test)  #np.array([np.asarray(i) for i in x_test])
y_train_tens = np.array(y_train) #np.array([np.asarray(i) for i in y_train])
y_test_tens  = np.array(y_test)  #np.array([np.asarray(i) for i in y_test])

# data_np = np.asarray(data, np.float32)

# data_tf = tf.convert_to_tensor(data_np, np.float32)

# Train the model
model.fit(x_train_tens, y_train_tens, batch_size=32, epochs=8, verbose=2, shuffle=True)

# Evaluate using the test data set
model.evaluate(x_test_tens, y_test_tens, batch_size=32, verbose=2)

print(model.summary())

# print('Done')