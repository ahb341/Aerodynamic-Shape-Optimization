import random
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

# Preprocess Data
def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

data = np.load('aero_shape_opt\\datasets\\data_file_ann.npz',allow_pickle=True)
x_train = data['x_train']
x_test = data['x_test']
y_train = data['y_train']
y_test = data['y_test']

x_train_tens = np.array(x_train).astype(float) #np.array([np.asarray(i) for i in x_train])
x_test_tens  = np.array(x_test).astype(float)  #np.array([np.asarray(i) for i in x_test])
y_train_tens = np.array(y_train).astype(float) #np.array([np.asarray(i) for i in y_train])
y_test_tens  = np.array(y_test).astype(float)  #np.array([np.asarray(i) for i in y_test])

x_train = NormalizeData(x_train)
x_test = NormalizeData(x_test)
y_train = NormalizeData(y_train)
y_test = NormalizeData(y_test)

# Build ANN Model
def generate_ANN(input, output):
   # ANN Model
   # Input - an arbitrary vector to size the input of the ANN

   # input = np.array([af.interp_x,af.interp_y]).flatten('F')

   model = tf.keras.Sequential(
   [
      tf.keras.layers.Input(shape=(len(input),)),
      tf.keras.layers.BatchNormalization(),
      tf.keras.layers.Dense(20, activation='relu'),
      tf.keras.layers.BatchNormalization(),
      tf.keras.layers.Dense(10, activation='relu'),
      tf.keras.layers.BatchNormalization(),
      #tf.keras.layers.Dropout(0.20),
      # tf.keras.layers.Dense(25, activation='relu'),
      # tf.keras.layers.Dropout(0.15),
      # tf.keras.layers.Dense(20, activation='relu'),
      # tf.keras.layers.Dropout(0.15),

      tf.keras.layers.Dense(1, activation='linear')
      #tf.keras.layers.Dense(len(output), activation='softmax')
      #tf.keras.layers.Dense(1, activation='softmax')
   ])

   model.compile(optimizer=keras.optimizers.Adam(lr=0.001),
               loss='mse',
               metrics=['mae'])

   model.summary()

   return model

model = generate_ANN(x_train[0],y_train[0])

# data_np = np.asarray(data, np.float32)

# data_tf = tf.convert_to_tensor(data_np, np.float32)

# Train the model
#model.fit(x_train_tens, y_train_tens, batch_size=32, epochs=8, verbose=2, shuffle=True)
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=32, epochs=5, verbose=2, shuffle=True)

def plot_metric(history, metric):
    train_metrics = history.history[metric]
    val_metrics = history.history['val_'+metric]
    epochs = range(1, len(train_metrics) + 1)
    plt.plot(epochs, train_metrics)
    plt.plot(epochs, val_metrics)
    plt.title('Training and validation '+ metric)
    plt.xlabel("Epochs")
    plt.ylabel(metric)
    plt.legend(["train_"+metric, 'val_'+metric])
    plt.show()

plot_metric(history,'loss')

# Evaluate using the test data set
#model.evaluate(x_test_tens, y_test_tens, batch_size=32, verbose=2)
#model.evaluate(x_test, y_test, batch_size=32, verbose=2)

print(model.summary())

print('Done')